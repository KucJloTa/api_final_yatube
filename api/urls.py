from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')
router.register('follow', FollowViewSet, basename='follow')
router.register('group', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
]
