from django.conf import settings 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request



class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request):
        return super().authenticate(request)


        