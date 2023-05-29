from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserSerializer)
from .models import User


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Выполните здесь дополнительные действия, связанные с аутентификацией пользователя
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request):
        # Выполните здесь действия, связанные с выходом пользователя
        return Response(status=status.HTTP_200_OK)
