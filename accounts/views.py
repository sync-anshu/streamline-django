from pyairtable import Api
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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

