from rest_framework import generics
from rest_framework.response import Response
from users import serializers

class RegisterApi(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": serializers.UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )
