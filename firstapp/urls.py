from django.urls import path
from . import views
urlpatterns = [
        path('firstapp/',views.hello,name="hello"),
]