import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


def get_headers():
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "apikey": settings.ATTOM_API_KEY
    }
    return headers


class PropertyList(APIView):
    def get(self, request):
        # Get prepared to call Attom property list API.
        headers = get_headers()
        url = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/address?postalcode=82009&page=1&pagesize=100'
        response = None
        try:
            response = requests.get(url=url, headers=headers)
            json_response = response.json()
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception:
            return Response('Something was wrong about this property list API.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PropertyDetail(APIView):
    def get(self, request, attom_id):
        headers = get_headers()
        # 228520
        url = ('https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/detail?attomid={}'.format(attom_id))
        response = None
        try:
            response = requests.get(url=url, headers=headers)
            json_response = response.json()
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception:
            return Response('Something was wrong about this property detail API.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
