from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, PostsViewSet

router = DefaultRouter()

router.register(
    'posts', PostsViewSet, basename='posts'
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='posts_comments'
)
router.register(
    r'comments/(?P<comment_id>\d+)/comments',
    CommentsViewSet,
    basename='posts_comments'
)

urlpatterns = (
    path('', include(router.urls)),
)
