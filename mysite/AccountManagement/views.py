from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, permissions
import django_filters.rest_framework
from rest_framework import status
from AccountManagement.serializers import *
# Create your views here.


class createAccount(generics.CreateAPIView):
    serializer_class = RegisterAccount
    permission_classes = [permissions.AllowAny]


class AccountList(generics.ListCreateAPIView):
    serializer_class = AccountSerializerAdmin
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username']

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return Account.objects.all()
        # return Response('You do not have rights on the page')
        else:
            return Account.objects.filter(id=self.request.user.id)


class OptionsAccountListAdmin(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializerAdmin

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return Account.objects.all()


# class ChangePasswordAdmin(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ChangePasswordSerializer
#
#     def get_queryset(self):
#         if self.request.user.is_superuser is True:
#             return Account.objects.all()
#         return Account.objects.filter(id=self.request.user.id)

class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OptionsAccountUser(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializerUser

    def get_object(self):
        obj = self.request.user
        return obj
