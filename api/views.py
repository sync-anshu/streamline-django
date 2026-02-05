from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access = response.data['access']
            refresh = response.data['refresh']
           
            response.set_cookie(
                key='access',
                value=access,
                domain="domain.streamline.com" if not settings.DEBUG else None,
                path="/",
                max_age= 60 * 5,
                httponly=True,
                secure=True,
                samesite="Lax"
              
            )

            response.set_cookie(
                key='refresh',
                value=refresh,
                domain="domain.streamline.com" if not settings.DEBUG else None,
                path='/',
                max_age= 60 * 60 * 24 * 30,
                httponly=True,
                secure=True,
                samesite="Lax"
            )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        try:
            response = super().post(request, *args, **kwargs)
        except Exception as e:
            return Response(data={'detail': 'Auth Failed loser'}, status=status.HTTP_401_UNAUTHORIZED)

        if response.status_code == 200:
            access = response.data.get('access')
            response.set_cookie(
                key='access',
                value=access,
                domain="domain.streamline.com" if not settings.DEBUG else None,
                path="/",
                max_age= 60 * 5,
                httponly=True,
                secure=True,
                samesite="Lax"
            )
        return response