from django.http import Http404
from rest_framework.permissions import BasePermission

from ads.models import Ad, Comment
from users.models import UserRoles


class AdEditPermission(BasePermission):
    """
    Разрешение на редактирование объявления только для владельца объявления или админа.
    """
    message = "Only owner or admin can edit ads"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True

        try:
            ad = Ad.objects.get(pk=view.kwargs['pk'])
        except Ad.DoesNotExist:
            raise Http404

        if ad.author_id == request.user.id:
            return True
        return False


class CommentEditPermission(BasePermission):
    """
    Разрешение на редактирование комментариев только для его владельца или админа.
    """
    message = "Only owner or admin can edit comments"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True

        try:
            comment = Comment.objects.get(pk=view.kwargs['pk'])
        except Comment.DoesNotExist:
            raise Http404

        if comment.author_id == request.user.id:
            return True
        return False
