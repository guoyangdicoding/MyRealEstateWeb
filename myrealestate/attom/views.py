from attom.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from attom.serializers import *


class PropertyList(APIView):
    def get(self, request):
        # Get prepared to call Attom property list API.
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response({'message': 'successful', 'data': serializer.data}, status=status.HTTP_200_OK)


class PropertyDetail(APIView):
    def get(self, request, id):
        try:
            properties = Property.objects.get(id=id)
            serializer = PropertySerializer(properties)
            return Response({'message': 'successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Property.DoesNotExist:
            return Response({'message': 'The passed-in property ID does not exist.', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
