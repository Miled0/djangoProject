from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('members/',views.member,name="member"),
    path('members/details/<int:id>',views.details,name="details"),
    path('test/',views.test,name='test'),
]