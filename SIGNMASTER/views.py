from django.contrib.auth.hashers import make_password
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render
import cv2
import mediapipe as mp
import numpy as np
import math
import random
from keras.models import load_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from rest_framework.utils import json

from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Player
from django.http import JsonResponse






# 액션 목록과 모델 불러오기
actions = ['hello', 'pretty', 'shy', 'introduce', 'sorry', 'good', 'how much', 'fine', 'thanks', 'please']
seq_length = 30
model = load_model('models/0518_02.h5')

# MediaPipe hands 모델 초기화
mp_hands = mp.solutions.hands

try:
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
except Exception as e:
    print(f"Failed to initialize MediaPipe Hands: {e}")
mp_drawing = mp.solutions.drawing_utils

# 비디오 캡처 초기화
cap = cv2.VideoCapture(0)

seq = []
action_seq = []

# 전역 변수로 예측된 동작을 저장할 변수 생성
predicted_action = None

current_action = None  # 현재 선택된 랜덤 액션


def select_random_action():
    """랜덤 액션을 선택하여 반환합니다."""
    return random.choice(actions)

def get_new_action(request):
    global current_action
    current_action = select_random_action()  # 새로운 랜덤 액션 선택
    return JsonResponse({'new_action': current_action})


def gen_frames():
    global predicted_action
    seq = []
    action_seq = []

    while cap.isOpened():
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)
        img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks:
            add = np.full((31,), -1)
            left_loc_x, left_loc_y, right_loc_x, right_loc_y = 0, 0, 0, 0

            for res, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
                hand_side = handedness.classification[0].label
                joint = np.zeros((21, 4))

                for j, lm in enumerate(res.landmark):
                    joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

                v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :3]
                v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], :3]
                v = v2 - v1
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
                angle = np.degrees(np.arccos(
                    np.einsum('nt,nt->n', v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
                              v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :])))

                if hand_side == "Left":
                    add[:15] = angle
                    left_loc_x = int(res.landmark[mp_hands.HandLandmark.WRIST].x * img.shape[1])
                    left_loc_y = int(res.landmark[mp_hands.HandLandmark.WRIST].y * img.shape[0])

                if hand_side == "Right":
                    add[15:-1] = angle
                    right_loc_x = int(res.landmark[mp_hands.HandLandmark.WRIST].x * img.shape[1])
                    right_loc_y = int(res.landmark[mp_hands.HandLandmark.WRIST].y * img.shape[0])

                distance = math.sqrt((left_loc_x - right_loc_x) ** 2 + (left_loc_y - right_loc_y) ** 2)
                add[-1] = distance if left_loc_x and right_loc_x else 0

                seq.append(add)
                mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

                if len(seq) < seq_length:
                    continue

                input_data = np.expand_dims(np.array(seq[-seq_length:], dtype=np.float32), axis=0)
                y_pred = model.predict(input_data).squeeze()
                i_pred = int(np.argmax(y_pred))
                conf = y_pred[i_pred]

                if conf >= 0.9:
                    action = actions[i_pred]
                    action_seq.append(action)
                    if len(action_seq) >= 3 and action_seq[-1] == action_seq[-2] == action_seq[-3]:
                        predicted_action = action  # 예측된 동작을 전역 변수에 저장


        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def get_predicted_action(request):
    global predicted_action, current_action

    # 현재 로그인된 사용자의 score 업데이트
    if predicted_action == current_action:
        user = request.user
        user.score += 1
        user.save()

    return JsonResponse({'action': predicted_action, 'score': request.user.score})


def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


def index(request, nickname):
    global current_action, predicted_action

    # 새로운 랜덤 액션 선택
    new_action = select_random_action()
    if current_action != new_action:
        current_action = new_action
        predicted_action = None  # 새로운 액션이 설정될 때 예측된 액션 초기화

    # 예측된 액션과 현재 액션을 템플릿으로 전달
    return render(request, 'signmaster/index.html', {
        'user': request.user,  # 사용자 정보 전달
        'predicted_action': predicted_action,  # 예측된 액션 전달
        'current_action': current_action,  # 랜덤 액션 전달
        'nickname': nickname
    })


class Login(APIView):
    def get(self, request):
        return render(request, "signmaster/login.html")

    def post(self, request):
        # 로그인 처리
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        print(email)
        print('옴')

        user = User.objects.filter(email=email).first()
        print(user)

        if user is None:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))

        if user.check_password(password):
            # 로그인이 성공했을 때
            login(request, user)  # Django의 login 함수 사용
            print('로그인은 성공')
            return Response(status=200)
        else:
            print('로그인은 실패')
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))

class Signup(APIView):
    def get(self, request):
        return render(request, "signmaster/signup.html")

    def post(self, request):
        try:
            # 회원가입 로직
            email = request.data.get('email', None)
            password = request.data.get('password', None)
            username = request.data.get('username', None)
            print(email, password, username)

            # 필수 필드 확인
            if not all([email, password, username]):
                raise APIException("모든 필드를 채워주세요.")

            # 사용자 생성
            User.objects.create(email=email,
                                username=username,
                                password=make_password(password),
                                score=0)
            print('넘어 온다')

            # 리다이렉션 URL 포함 응답 반환
            return Response({'message': '회원가입 성공', 'redirect_url': '/login/'}, status=200)

        except Exception as e:
            # 예외 처리
            return Response({'message': str(e)}, status=400)


def selectoption_view(request):
    return render(request, 'signmaster/selectoption.html')


def learn_sign_language_view(request):
    return render(request, 'signmaster/learn_sign_language.html')

def learn_word_view(request, word):
    # 각 단어에 대한 설명과 비디오 파일 경로 설정
    word_data = {
        '안녕하세요': {
            'description': '주먹을 쥔 채 양손을 들어 손의 바닥면이 바깥을 보이게 한다.',
            'video_filename': 'hello.mp4'
        },
        '예쁘다': {
            'description': '한손을 주먹을 쥔 채 검지손가락만 피고 볼에 가져다 댄다.',
            'video_filename': 'pretty.mp4'
        },
        '부끄럽다': {
            'description': '부끄러워서 볼이 빨갛게 물드는 모습을 연상한다.',
            'video_filename': 'shy.mp4'
        },
        '내 소개를 할게요': {
            'description': '나 + 소개 + 합니다를 합친 문장이다.',
            'video_filename': 'introduce.mp4'
        },
        '미안합니다': {
            'description': '엄지와 검지를 손에 이마에다 대고 손을 받쳐서 마무리한다.',
            'video_filename': 'sorry.mp4'
        },
        '좋습니다': {
            'description': '주먹을 쥔 한 손을 코에다 가져다 댄다.',
            'video_filename': 'good.mp4'
        },
        '이거 얼마예요?': {
            'description': '이거 + 얼마예요를 합친 문장이다.',
            'video_filename': 'howmuch.mp4'
        },
        '괜찮습니다': {
            'description': '새끼손가락만 펴고 턱밑에 가져다 댄다.',
            'video_filename': 'fine.mp4'
        },
        '감사합니다': {
            'description': '손 끝을 잘 서라도 은혜를 갚을만큼 감사한 모습을 연상한다.',
            'video_filename': 'thanks.mp4'
        },
        '부탁해요': {
            'description': '상대에게 악수하듯 손을 흔들어 부탁하는 모습을 연상한다.',
            'video_filename': 'please.mp4'
        },
    }

    # 선택된 단어에 해당하는 데이터를 가져오기
    word_info = word_data.get(word, {'description': '해당 단어에 대한 정보가 없습니다.', 'video_filename': ''})

    # 비디오 파일의 경로 설정
    video_url = f'{word_info["video_filename"]}' if word_info["video_filename"] else ''

    # 템플릿에 전달할 컨텍스트 설정
    context = {
        'word': word,
        'description': word_info['description'],
        'video_url': video_url,
    }

    return render(request, 'signmaster/learn_word.html', context)


def make_name_view(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        if nickname:
            return redirect('test_page', nickname=nickname)  # test 페이지로 리다이렉트

    return render(request, 'signmaster/make_name.html')
