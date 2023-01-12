from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ExampleEndPoint(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = {"data" : "xxxxxx",
                    "name" : "Name Test"}
        return Response(response)
