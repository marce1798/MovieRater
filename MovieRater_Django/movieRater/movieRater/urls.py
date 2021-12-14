from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import router_user

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Rater - ApiDoc",
        default_version='v1',
        description="Documentación de la api de Movie Rater",
        terms_of_service='https://www.google.com/polices/terms/',
        contact=openapi.Contact(email="vivasmarcelo393@gmail.com"),
        license=openapi.License(name="BDS License"),
    ),
    public = True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/',include(router_user.urls)),
]
