from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from calendifa.views import StatusView

schema_view = get_schema_view(
    openapi.Info(
        title="Persian Jalali Calendar",
        default_version="V1",
        description="Api endpopints for calendifa",
        contact=openapi.Contact(email="khavari.7878@yahoo.com"),
        license=openapi.License(name="MIT Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "v1/status/",
        StatusView.as_view(),
        name="Status",
    ),
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "v1/calendar/",
        include("calendifa.urls"),
    ),
]
