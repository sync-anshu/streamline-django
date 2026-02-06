from pyairtable import Api
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status



api = Api(settings.AIRTABLE_API_KEY)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(request: Request) -> Response:
    table = api.table('appvOFmpLj8ZNNGPR', 'tbl25IPMcnCR5bOIR')  
    response = table.all()
    return Response(response, status=status.HTTP_200_OK)


from rest_framework.views import APIView
from accounts.models import AirTableUser as User
from accounts.serializers import SignUpSerializer

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.email for user in User.objects.all()]
        return Response(usernames)


class SignUp(APIView):
    """
    View to sign up a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)