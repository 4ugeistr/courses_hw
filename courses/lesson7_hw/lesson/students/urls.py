from django.contrib import admin
from django.urls import path
from students.views import MyView, MyViewWithPK

urlpatterns = [
    path('view/', MyView.as_view()),
    path('view/<pk>/', MyViewWithPK.as_view()),
]
