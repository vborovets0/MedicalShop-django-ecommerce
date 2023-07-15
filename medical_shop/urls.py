from django.urls import path

from medical_shop.views import home

urlpatterns = [
    path("", home)
]


app_name = "medical_shop"
