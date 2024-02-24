from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    FreelanceSignupSerializer,
    ClientSignupSerializer,
)
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsFreelancer, IsClient
from rest_framework.authtoken.views import ObtainAuthToken


class FreelanceSignUpView(generics.GenericAPIView):
    serializer_class = FreelanceSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "User": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": Token.objects.get(user=user).key,
                "message": "account created succssefully",
            }
        )


class ClientSignUpView(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "User": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": Token.objects.get(user=user).key,
                "message": "account created succssefully",
            }
        )


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}  # Fix the context argument
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "is_client": user.is_client}
        )


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            Token.objects.filter(user=user).delete()
            return Response(
                {"message": "Logged out successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "User is not authenticated."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class FreelancerDashboard(APIView):
    permission_classes = [IsFreelancer]

    def get(self, request, *args, **kwargs):
        return Response({"message": "You are a Freelancer."})


class ClientDashboard(APIView):
    permission_classes = [IsClient]

    def get(self, request, *args, **kwargs):
        return Response({"message": "You are a Client."})
