from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Comments, Posts
from .permission import IsOwnerOrReadOnly
from .serializers import CommentsSerializer, PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.annotate(comments_count=Count('comments'))
    serializer_class = PostsSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        comment_id = self.kwargs.get('comment_id')
        if comment_id:
            parent_comment = get_object_or_404(Comments, id=comment_id)
            return parent_comment.children_comments.annotate(
                children_comments_count=Count('children_comments')
            )
        else:
            post_id = self.kwargs.get('post_id')
            post = get_object_or_404(Posts, id=post_id)
            return post.comments.annotate(
                children_comments_count=Count('children_comments')
            )

    def perform_create(self, serializer):
        comment_id = self.kwargs.get('comment_id')
        if comment_id:
            parent_comment = get_object_or_404(Comments, id=comment_id)
            serializer.save(
                author=self.request.user,
                parent=parent_comment
            )
        else:
            post_id = self.kwargs.get('post_id')
            post = get_object_or_404(Posts, id=post_id)
            serializer.save(
                author=self.request.user,
                post=post
            )
