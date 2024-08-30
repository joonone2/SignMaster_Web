from django.conf import settings
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime, timedelta

class AutoLogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            # 사용자가 인증되지 않은 경우, 아무것도 하지 않음
            return

        # 마지막 활동 시간을 세션에 저장
        last_activity = request.session.get('last_activity')

        # 현재 시간을 세션에 저장
        now = datetime.now()

        if last_activity:
            # 마지막 활동 시간 가져오기
            last_activity_time = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')

            # 마지막 활동 이후 경과된 시간 계산
            elapsed_time = now - last_activity_time

            # 세션 타임아웃(예: 10분) 초과 시 자동 로그아웃
            if elapsed_time > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                logout(request)
                request.session.flush()
        request.session['last_activity'] = now.strftime('%Y-%m-%d %H:%M:%S.%f')
