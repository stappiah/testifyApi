from rest_framework import generics, permissions, authentication, status
from .serializers import AccountSerializer, AccountPropertiesSerializer
from .models import Account
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import check_password


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)


class CustomAuthModel(ObtainAuthToken):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone_number": user.phone_number,
                "token": token.key,
                "user_id": user.pk,
                "response": "Login successfully",
            }
        )


class ManageAccountView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AccountPropertiesSerializer
    queryset = Account.objects.all()


class ChangePassword(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Account.objects.all()

    def update(self, request, *args, **kwargs):
        user = self.request.user
        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")

        if not check_password(current_password, user.password):
            return Response(
                {"current_password": "Current password is incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()
        return Response(
            {"message": "Password successfully changed"}, status=status.HTTP_200_OK
        )
