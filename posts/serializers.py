from rest_framework import serializers

from .models import Comments, Posts


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'author',
            'image',
            'text',
            'pub_date',
            'comments_count',
        )
        model = Posts


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    children_comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'id',
            'author',
            'image',
            'text',
            'pub_date',
            'children_comments_count',
        )
        model = Comments
