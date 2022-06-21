from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from ads.filters import AdModelFilter
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.permissions import AdEditPermission, CommentEditPermission

from rest_framework.permissions import AllowAny, IsAuthenticated


@extend_schema_view(
    list=extend_schema(description="Retrieve ads list",
                       summary="Ads list"),
    create=extend_schema(description="Create new ad",
                         summary="Create ad"),
    retrieve=extend_schema(description="Detail ad view",
                           summary="Retrieve ad"),
    update=extend_schema(description="Update ad",
                         summary="Update ad"),
    partial_update=extend_schema(description="Partially update ad",
                                 summary="Update ad"),
    destroy=extend_schema(description="Delete ad",
                          summary="Delete ad"),
)
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdModelFilter
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()

        return Ad.objects.all()

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [AdEditPermission, IsAuthenticated]
        return super(self.__class__, self).get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "retrieve", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer


@extend_schema_view(
    list=extend_schema(description="Retrieve comments list",
                       summary="Comments list"),
    create=extend_schema(description="Create new comment",
                         summary="Create comment"),
    retrieve=extend_schema(description="Detail comment view",
                           summary="Retrieve comment"),
    update=extend_schema(description="Update comment",
                         summary="Update comment"),
    partial_update=extend_schema(description="Partially update comment",
                                 summary="Update comment"),
    destroy=extend_schema(description="Delete comment",
                          summary="Delete comment"),
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, pk=ad_pk)
        user = self.request.user
        serializer.save(author=user, ad=ad)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [CommentEditPermission, IsAuthenticated]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        ad_pk = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, pk=ad_pk)
        return ad.comments.all()
