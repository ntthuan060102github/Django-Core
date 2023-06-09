from django.urls import path, include
from django_app.views.health import Health
from django_app.app_configs import app_configs as av
from django_app.routers.user import urls as user_urls
from django_app.routers.auth import urls as auth_urls
from django_app.routers.health import urls as health_router
from app_core.swagger import urls as swagger_urls

urls = health_router + user_urls + auth_urls
urlpatterns = [path(f"{av.API_PREFIX}/", include(urls))] + swagger_urls
handler404 = Health().not_found