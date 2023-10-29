from rest_framework import viewsets, filters, permissions
from .models import Employee, Asset, Repair, Transfer
from .serializers import UserSerializer, EmployeeSerializer, AssetSerializer, RepairSerializer, TransferSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .auth import AUTH_CLASS
from .permissions import IsAuthenticatedOrPostOnly


class CustomLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user': UserSerializer(user).data
        })


class UserViewSet(viewsets.ModelViewSet):
    model = User
    authentication_classes = [AUTH_CLASS]
    permission_classes = [IsAuthenticatedOrPostOnly]
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]


class EmployeeViewSet(viewsets.ModelViewSet):
    model = Employee
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]


class AssetViewSet(viewsets.ModelViewSet):
    model = Asset
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer
    filter_backends = [filters.OrderingFilter]


class RepairViewSet(viewsets.ModelViewSet):
    model = Repair
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RepairSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['asset']


class TransferViewSet(viewsets.ModelViewSet):
    model = Transfer
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransferSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['asset']