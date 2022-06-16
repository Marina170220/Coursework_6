from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = []


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass
