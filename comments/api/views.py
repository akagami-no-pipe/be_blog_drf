from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from comments.models import Comment
from comments.api.serializers import CommentSerializer

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filterset_fields = ['post']