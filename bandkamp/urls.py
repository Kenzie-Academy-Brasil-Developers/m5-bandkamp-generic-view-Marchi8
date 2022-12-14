from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("albums.urls")),
    path("api/docs/schema", SpectacularAPIView.as_view(), name="docs"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="docs"),
        name="swagger-ui",
    ),
    path(
        "api/docs/redoc/",
        SpectacularRedocView.as_view(url_name="docs"),
        name="redoc",
    ),
]
