from django.urls import path
from . import views

urlpatterns = [
    path('', views.SendEmail, name="send_mail"),
]