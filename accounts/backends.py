from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from pyairtable import Api
from accounts.utils import match_airtable_user

api = Api(settings.AIRTABLE_API_KEY)
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
            #SHM - get all accounts from airtable
            found, allow_access = match_airtable_user(username)

            if not found or not allow_access:
                return None

            #if the user is not found, return None
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