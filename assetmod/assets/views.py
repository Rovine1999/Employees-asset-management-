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


# CustomLogin class is used to override the default login view
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

# UserViewSet is used to view and edit user details
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [IsAuthenticatedOrPostOnly]
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]

# EmployeeViewSet is used to view and edit employee details
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]

# AssetViewSet is used to view and edit asset details
class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer
    filter_backends = [filters.OrderingFilter]

# RepairViewSet is used to view and edit repair details
class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RepairSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    filterset_fields = ['asset']

# TransferViewSet is used to view and edit transfer details
class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransferSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    filterset_fields = ['asset']