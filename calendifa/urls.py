from django.urls import path
from . import views


urlpatterns = [
    path("now/english/", views.NowView.as_view({'get': 'list'}), name="Now"),
    path("now/persian/", views.NowPersianDigitView.as_view(), name="NowPersianDigit"),
]
