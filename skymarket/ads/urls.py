from django.urls import include, path

from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet
from rest_framework_nested.routers import NestedSimpleRouter

ads_router = SimpleRouter()
ads_router.register(r"ads", AdViewSet, basename="ads")

comments_router = NestedSimpleRouter(ads_router, r"ads", lookup="ad")
comments_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),

]
