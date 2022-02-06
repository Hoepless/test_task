from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        author = request.user
        commented = Comment.objects.create(author=author, **validated_data)
        return commented

    def to_representation(self, instance):
        """
        To represent name of author instead of ID
        """
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username
        return representation


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        """
        assigning authorized author
        """
        request = self.context.get("request")
        author = request.user
        posted = Post.objects.create(author=author, **validated_data)
        return posted

    def to_representation(self, instance):
        """
        To represent name of author instead of ID
        """
        action = self.context.get('action')
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username
        if action == 'retrieve':
            representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        elif action == 'list':
            representation['comments'] = instance.comments.count()
        return representation
