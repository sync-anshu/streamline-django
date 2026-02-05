from pyairtable import Api
from django.conf import settings
from django.http import JsonResponse

api = Api(settings.AIRTABLE_API_KEY)

def test(request):
    table = api.table('appvOFmpLj8ZNNGPR', 'tbl25IPMcnCR5bOIR')  
    response = table.all()
    return JsonResponse(response, safe=False)

