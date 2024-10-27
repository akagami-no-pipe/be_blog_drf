
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import PostPermissions

class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, PostPermissions]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    filterset_fields = ['title', 'category', 'category__slug']
    lookup_field = 'slug'
