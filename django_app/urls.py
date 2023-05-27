from drf_yasg import openapi
from django.urls import re_path, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from django_app.views.user import UserView

schema_view = get_schema_view(
   openapi.Info(
      title="API Document for Django Core",
      default_version='v1.0.0',
      description="API Document for Django Core",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ntthuan060102.work@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$', 
        schema_view.without_ui(cache_timeout=0), 
        name='schema-json'
    ),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('user/', UserView.as_view({'get': 'retrieve', 'post': 'create'})),
]

# handler404 = custom404