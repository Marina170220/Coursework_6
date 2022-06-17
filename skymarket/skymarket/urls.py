from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# TODO здесь необходимо подключить нужные нам urls к проекту
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("", include("users.urls")),
    path("", include("ads.urls")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/docs/', SpectacularAPIView.as_view(), name='docs'),
    path('api/docs/swagger-ui/', SpectacularSwaggerView.as_view(url_name='docs'), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)