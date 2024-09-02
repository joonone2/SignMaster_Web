# ✋ 수어 교육용 앱서비스 - SignMaster

SignMaster는 청각장애인과 비장애인을 위한 수어 교육 플랫폼입니다. 간단한 수어 학습부터 실전 테스트까지, 사용자가 수어를 쉽고 효율적으로 배울 수 있도록 돕습니다. 다양한 수어 언어를 지원하며, 사용자 맞춤형 학습과 실시간 피드백 기능을 제공합니다.

## 📌 주요 기능
- **수어 배우기**: 다양한 언어의 수어를 동영상 강의와 함께 학습할 수 있습니다.
- **수어 테스트**: 배운 내용을 테스트하여 학습의 효과를 확인할 수 있습니다.
- **닉네임 설정**: 개인화된 학습 환경을 위해 사용자 설정 기능을 제공합니다.
- **맞춤형 학습**: AI가 개인 학습 패턴을 분석해 맞춤형 교육을 제공합니다.

## 🖥️ Service UI
  
|                                                        기능선택                                                       |                                                         배우고 싶은 수어 선택                                                         |
| :---------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |
| <img src='https://github.com/user-attachments/assets/57bb11d0-6de4-403f-a0eb-0b6f2ba2b200'> | <img src='https://github.com/user-attachments/assets/22dcc97d-f2b6-47da-a137-7b531219d9ee'> |
|                                                     <b>수어 배우기</b>                                                      |                                                <b>닉네임 설정</b>                                                |
| <img src='https://github.com/user-attachments/assets/c4ee4eef-b173-496d-a5b6-0c99ea3b8213'> | <img src='https://github.com/user-attachments/assets/32933405-3a0f-4c97-8453-90e0c3ee16c5'> |
|                                                     <b>수어 테스트</b>                                                      |                                                <b>수어 테스트(정답 시)</b>                                                |
| <img src='https://github.com/user-attachments/assets/2279b6a5-ad33-4326-ab79-c3621187be4c'> | <img src='https://github.com/user-attachments/assets/ca976a2f-52f5-45ce-9d01-f1b095dff40f'> |

## 🚀 프로젝트의 발전 방향
- **다양한 수어 언어 추가 지원**: 여러 국가의 수어를 추가로 지원하여 글로벌 사용자층을 넓혀갈 예정입니다.
- **수어 인식 정확도 개선**: AI 기술을 지속적으로 업그레이드해 수어 인식의 정확도를 높일 계획입니다.
- **실시간 소통 기능 도입**: 수어 번역을 실시간으로 제공하여 즉각적인 소통을 지원할 예정입니다.
- **수어 교육 커뮤니티 활성화**: 사용자 간 학습 교류와 지원을 촉진하는 커뮤니티 기능을 강화할 것입니다.
- **AI 기반 맞춤형 학습 제공**: 각 사용자의 학습 패턴에 맞춰 개인화된 교육 콘텐츠를 제공할 예정입니다.

## ❓ 자주 묻는 질문 (FAQ)
- **수화 인식 기술의 정확도는 얼마나 되나요?**  
  SignMaster의 수화 인식 기술은 현재 96%의 정확도를 자랑하며, 지속적으로 개선하고 있습니다.
  
- **향후 추가 기능 계획이 있나요?**  
  네, 다양한 수화 언어 추가 지원, 실시간 소통 기능, 그리고 AI 기반 맞춤형 학습 기능을 도입할 계획입니다.

- **수화 초보자도 쉽게 사용할 수 있나요?**  
  네, 초보자도 쉽게 따라할 수 있도록 동영상 강의를 제공하고 있습니다.



<br>  
<br>  
<br>  
<br>  
<br>  
<br>  
<br>  
<br>  





  
# ✋ 수화 인식 모델 학습




## OpenCV와 MediaPipe를 사용한 각도 계산

이 프로젝트에서는 OpenCV와 MediaPipe를 사용하여 각 손가락 관절 간의 각도를 계산합니다. MediaPipe를 사용하여 손의 랜드마크를 추출한 후, 각 랜드마크 간의 벡터를 계산하고, 벡터 간의 각도를 구하는 방식으로 각도를 측정합니다. 이러한 각도 데이터는 각 손의 상대거리와 함께 모델의 입력 데이터로 사용됩니다.

<br>
<br>


## 프로젝트의 전체적인 흐름
데이터 준비: 손의 랜드마크 데이터와 관절 간의 각도를 준비합니다. 각 데이터 포인트는 왼손과 오른손의 랜드마크 좌표 및 각도 데이터로 구성된 1차원 배열입니다. <br>

모델 학습: LSTM 모델을 사용하여 데이터를 학습합니다. LSTM 레이어는 시퀀스 데이터를 처리하고, Dense 레이어는 학습된 패턴을 기반으로 손의 제스처를 분류합니다.<br>

제스처 예측: 학습된 모델을 사용하여 새로운 손의 랜드마크 데이터와 각도 데이터에 대해 제스처를 예측합니다.<br>


## Dataset

  - Dataset은 10개의 class, class 당 2개의 video, video당 약 900 frames (30초, 1초당 30frame)
  
    0. hello<br>
    1. pretty<br>
    2. shy<br>
    3. introduce<br>
    4. sorry<br>
    5. good<br>
    6. how much<br>
    7. fine<br>
    8. thanks<br>
    9. please<br>



    <hr>
### 이 프로젝트의 데이터셋은 손의 랜드마크간의 각도와 각 손의 상대거리를 담고 있습니다. 
### 각 데이터 포인트는 관절간의 각도를 포함하는 31개 요소의 1차원 배열로 표현됩니다. 데이터셋은 다음과 같은 방식으로 구성됩니다:


  왼손: 배열의 처음 15개의 인덱스에 왼손의 손가락간의 각도들이 할당됩니다.<br>

  오른손: 배열의 16번째 인덱스부터 15개의 인덱스에 오른손의 손가락간의 각도들이 할당됩니다.
<br>
  왼손과 오른손사이의 거리 : 마지막 인덱스에 입력됩니다.
<br>


  
  만약 왼손만 감지되었다면 오른손의 인덱스는 -1으로 채워집니다.
  
  ![image](https://github.com/joonone2/SignMaster/assets/129241680/7c9e7534-1753-407f-87f1-df19e78319fe)

  
  만약 오른손만 감지되었다면 왼손의 인덱스는 -1으로 채워집니다.
  
  ![image](https://github.com/joonone2/SignMaster/assets/129241680/105e5a4b-33c7-41d8-bf7c-22e2a9a8723d)

  
  두 손이 모두 감지되었다면 양쪽 손의 데이터가 모두 배열에 포함됩니다.
  
  ![image](https://github.com/joonone2/SignMaster/assets/129241680/392668ec-66db-462b-98c1-67e54e90de8f)



  
  <br>

  Dataset은 임의로 train 7099개 (90%), test 789개 (10%) 로 나눴습니다.
  
  31개 요소의 1차원 배열을 30 frame씩 앞뒤로 29 frame씩 overlap 시킨 것을 한 clip으로 하고 한 video 를 여러 clip으로 나누어 clip 을 하나씩 model에 넣었습니다.


  
  
- # Model
  
  손의 랜드마크 데이터를 학습하기 위해 LSTM(Long Short-Term Memory) 모델을 사용합니다.
  

  ### LSTM (Long Short-Term Memory) 레이어
  설명: LSTM은 순환 신경망(RNN)의 한 종류로, 시계열 데이터나 순차 데이터를 처리하는 데 효과적입니다.
  사용 이유:
  기억력: LSTM은 긴 시퀀스 데이터에서 중요한 정보를 잊지 않고 기억할 수 있습니다.
  손 랜드마크 시퀀스 처리: 손의 랜드마크 데이터는 시간에 따라 연속적으로 변하기 때문에, 시퀀스 데이터로 취급할 수 있습니다. LSTM은 이러한 시퀀스 데이터의 패턴을 학습하는 데 적합합니다.
  
  ### Dense 레이어
  사용 이유:
  분류: LSTM 레이어의 출력은 Dense 레이어를 통해 각 클래스에 대한 확률로 변환됩니다. 이 프로젝트에서는 손의 움직임이나 제스처를 분류하기 위해 사용됩니다.
  Softmax 활성화 함수: Dense 레이어의 활성화 함수로 softmax를 사용하여, 각 클래스에 대한 확률을 계산합니다. 이를 통해 모델이 각 입력 시퀀스에 대해 가장 가능성이 높은 클래스를 예측할 수 있습니다.
  


  - LSTM과 FC layer를 거쳐 지나온 feature에 대한 Activation function으로 Softmax와 Logsoftmax를 비교하여 실험해 성능이 더 잘나온 softmax를 사용하였습니다.
  
  - Loss function은 categorical_crossentropy 와 MSELoss를 비교하여 실험한 결과 더 성능이 잘 나온 categorical_crossentropy를 사용했습니다.

  
  
- # Performance
  
  1. 각각의 동작당 30초의 데이터를 학습 시켰을때의 그래프입니다.
  
    ![image](https://github.com/joonone2/SignMaster/assets/129241680/96f3b244-62a1-4823-80d2-c7700faad023)
_가로축 = epoch , 왼쪽 세로축 = loss, 오른쪽 세로축 = accuracy_

<br><br>


  2. 각각의 동작당 60초의 데이터를 학습 시켰을때의 그래프입니다.
    ![image](https://github.com/joonone2/SignMaster/assets/129241680/a32714c0-216d-4f43-9756-032899d705e5)
_가로축 = epoch , 왼쪽 세로축 = loss, 오른쪽 세로축 = accuracy_




  ### 2번이 1번보다 성능이 좋았기 때문에 학습데이터는 60초의 dataset으로 구성하였습니다. 
  
# actions
  
|                                                        how much                                                        |                                                         inroduce                                                         |
| :---------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |
| <img src='https://github.com/joonone2/SignMaster/assets/129241680/a98ae2b9-1108-43a2-bd42-09eb8de39b50'> | <img src='https://github.com/joonone2/SignMaster/assets/129241680/2f899986-7237-4a87-9f94-9545b57930d2'> |
|                                                     <b>please</b>                                                      |                                                <b>sorry</b>                                                |
| <img src='https://github.com/joonone2/SignMaster/assets/129241680/ad239822-0ae5-48e4-bfa0-8e29f25baf85'> | <img src='https://github.com/joonone2/SignMaster/assets/129241680/4f779a5e-8b69-4581-a73a-5666cce89cf3'> |
|                                                     <b>thanks</b>                                                      |                                                <b>fine</b>                                                |
| <img src='https://github.com/joonone2/SignMaster/assets/129241680/be9e4471-5709-4174-a71f-fd3edefcd36f'> | <img src='https://github.com/joonone2/SignMaster/assets/129241680/15a0716d-2406-47bf-a573-0ba4311c1d50'> |
|                                                     <b>good</b>                                                      |                                                <b>pretty</b>                                                |
| <img src='https://github.com/joonone2/SignMaster/assets/129241680/4f313df2-2d84-4b1a-a18b-a9148d4babb3'> | <img src='https://github.com/joonone2/SignMaster/assets/129241680/1943e045-85d7-452f-8ae4-6990cb1fc63f'> |
|                                                     <b>hello</b>                                                      |                                                <b>shy</b>                                                |
| <img src='https://github.com/joonone2/SignMaster/assets/129241680/30051e5e-13ab-4a3a-b0f2-bc318137f135'> | <img src='https://github.com/joonone2/SignMaster/assets/129241680/5f01063c-5559-4fb4-b886-40f5716bbd2f'> |





## 🛠️ Skills

<img width="800px" src='https://github.com/joonone2/SignMaster/assets/129241680/5d9b8d2a-daf9-443f-81af-d313f6d1ca61'  alt="Skills"/>

    

