from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sizning loyihangiz nomi",
      default_version='v1',
      description="API hujjati",
      # contact=openapi.Contact(email="admin@example.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('accounts.urls')),  # o‘z url'laringizni qo‘shing
   # Swagger URL'lari
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Swagger UI
   path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]