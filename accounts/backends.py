from django.contrib.auth.backends import BaseBackend, UserModel
from django.contrib.auth import  get_user_model
from django.contrib.auth.models import User


class AirTableBackend(BaseBackend):
    """
    Authenticate against the AirTable API.
    """

    def authenticate(self, request, username=None, password=None):
        """
        authenticate() should check the credentials it gets and return a user object 
        that matches those credentials if the credentials are valid.
        If they’re not valid, it should return None.
        """
        try:
            print("Authenticating user with email: ", username)
            print("Password: ", password)

            UserModel = get_user_model()
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            
        except Exception:
            return None


        return None

    def get_user(self, user_id):
        """
        The get_user method takes a user_id – which could be a username, database ID or whatever, 
        but has to be the primary key of your user object 
        – and returns a user object or None. and returns a user object or None.
        """
        try:
            UserModel = get_user_model()
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None