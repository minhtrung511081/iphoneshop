from django.urls import *
from django.conf.urls import *
from Statistic import views
urlpatterns = [
    path('manageCategories/', views.manageCategories.as_view()),
    path('order/', views.order_view.as_view()),
    path('statistics/', views.statisticsView.as_view()),
    path('total/', views.totalView.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
