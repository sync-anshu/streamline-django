from django.urls import path
from .views import test, ListUsers, SignUp

urlpatterns = [
    path('test/', test, name='test'),
    path('users/', ListUsers.as_view(), name='users'),
    path('signup/', SignUp.as_view(), name='signup'),
]

