from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets

from ads.filters import AdModelFilter
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.permissions import AdEditPermission, CommentEditPermission


from rest_framework.permissions import AllowAny, IsAuthenticated


#
# class AdPagination(pagination.PageNumberPagination):
#     pass

# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdModelFilter
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [AdEditPermission, IsAuthenticated]
        return super(self.__class__, self).get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "retrieve", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [CommentEditPermission, IsAuthenticated]
        return super(self.__class__, self).get_permissions()
