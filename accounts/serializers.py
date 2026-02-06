from rest_framework import serializers
from accounts.models import AirTableUser as User
from pyairtable import Api
from django.conf import settings
from accounts.utils import get_airtable_user

api = Api(settings.AIRTABLE_API_KEY)


class SignUpSerializer(serializers.Serializer):
     email = serializers.EmailField()
     password = serializers.CharField(write_only=True)
     password_confirmation = serializers.CharField(write_only=True)

     def validate(self, attrs):
         if attrs['password'] != attrs['password_confirmation']:
             raise serializers.ValidationError("Passwords do not match")
         return attrs
     
     def create(self, validated_data):
        """
        Create a new user.
        """
        email =  validated_data['email']
        airtable_user = get_airtable_user(email)

        found = airtable_user is not None
        allow_access = airtable_user.get('fields',{}).get('Allow Access', False) if airtable_user else False

        if not found:
            raise serializers.ValidationError("User not found")

        if not allow_access:
            raise serializers.ValidationError("User does not have access")

        user = User.objects.create_user(
            email=email,
            password=validated_data['password'],
            airtable_id=airtable_user.get('id') if airtable_user else None
        )
        return user