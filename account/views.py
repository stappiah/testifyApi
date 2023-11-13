from rest_framework import generics, permissions, authentication
from .serializers import AccountSerializer, AccountPropertiesSerializer
from .models import Account
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)


class CustomAuthModel(ObtainAuthToken):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone_number': user.phone_number,
            'token': token.key,
            'user_id': user.pk,
            'response': 'Login successfully'
        })


class ManageAccountView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AccountPropertiesSerializer

    queryset = Account.objects.all()
