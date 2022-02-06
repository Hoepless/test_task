from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import F

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["post"], url_path="upvote")
    def upvote(self, request, pk):
        get_object_or_404(self.queryset, pk=pk)
        self.queryset.filter(pk=pk).update(upvotes=F("upvotes") + 1)
        serializer = self.get_serializer(self.queryset.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
