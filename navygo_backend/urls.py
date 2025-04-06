"""
URL configuration for navygo_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from reservation.views import CreateReservationViewSet, EditReservationViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/reservations/<uuid:id>",
        CreateReservationViewSet.as_view({"get": "retrieve"}),
    ),
    path(
        "api/reservations/",
        CreateReservationViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path("api/", include("transportation_service_manager.urls")),
    path("api/reservations/", EditReservationViewSet.as_view({"put": "update"})),
    # API schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

]
