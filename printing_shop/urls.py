from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Printing Shop API",
        default_version='v1',
        description="API documentation for Printing Shop",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@printingshop.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('warehouse.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('crm.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]