from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of apiView features."""

        an_apiview = [
            'aaaaaaaaaaaaaaaa',
            'bbbbbbbbbbbbbbbb',
            'cccccccccccccccc',
        ]

        return Response({'msg': 'Hello!', 'api': an_apiview})

    def post(self, request):
        """ Create a hello msg with my name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {0}".format(name)
            return Response({'message': msg})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating object."""

        return Response({'message': 'Put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes the object with pk"""

        return Response({'method': 'Delete'})
