from django.contrib import admin
from django.urls import path
from subject.views import MyView, MyViewWithPK

urlpatterns = [
    path('subjects/', MyView.as_view()),
    path('subjects/<pk>/', MyViewWithPK.as_view()),
]
