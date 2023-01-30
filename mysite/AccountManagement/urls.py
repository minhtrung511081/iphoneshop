from django.urls import *
from django.conf.urls import *
from AccountManagement import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('registerAccount/', views.createAccount.as_view()),
    url(r'^getToken/', obtain_jwt_token),
    path('accountList/', views.AccountList.as_view()),
    path('optionsAccountListAdmin/<int:pk>/', views.OptionsAccountListAdmin.as_view()),
    path('changePassword/', views.ChangePasswordView.as_view()),
    path('optionsAccountUser/', views.OptionsAccountUser.as_view()),
]
