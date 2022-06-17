from rest_framework import serializers

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=64, read_only=True)
    author_last_name = serializers.CharField(max_length=64, read_only=True)
    ad_id = serializers.PrimaryKeyRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)
    author_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at", "author_first_name", "author_last_name", "ad_id", "author_image"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=64, read_only=True)
    author_last_name = serializers.CharField(max_length=64, read_only=True)
    phone = serializers.CharField(max_length=128, read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author_id"]
