from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Return a list of apiView features."""

        an_apiview = [
            'aaaaaaaaaaaaaaaa',
            'bbbbbbbbbbbbbbbb',
            'cccccccccccccccc',
        ]

        return Response({'msg': 'Hello!', 'api': an_apiview})
