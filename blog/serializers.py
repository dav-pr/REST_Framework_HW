from rest_framework import serializers

from .models import Author, Comments, Posts, LikePost, LikeComments





class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Posts
        fields ='__all__'


class CommetnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = '__all__'

class LikeCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComments
        fields = '__all__'


