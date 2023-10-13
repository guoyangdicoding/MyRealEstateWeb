import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


def get_headers():
    """
    This method simply returns a headers for attom property api calls
    """
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "apikey": settings.ATTOM_API_KEY
    }
    return headers


def attom_property_get(url):
    """
    This method sends a GET API call to attom property back for property data.
    @param url, the GET property url (could be property list or property detail)
    @param **kwargs, some query parameters that may be passed in the GET API call.
    @return: response object containing information about the GET API call.
    """
    headers = get_headers()
    response = None
    try:
        response = requests.get(url=url, headers=headers)
        json_response = response.json()
        property_json = json_response.get('property', None)
        if not property_json:
            raise Exception('We did not get property list for some reason.')
        return property_json
    except Exception:
        raise Exception('Something was wrong about this Attom property GET API.')
