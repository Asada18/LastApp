from rest_framework import serializers

from .models import *


class StorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Stories
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'created_at', 'text', 'likes',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.email
        representation['images'] = PostImageSerializer(instance.images.all(),
                                                       many=True, context=self.context).data
        representation['post_comments'] = PostCommentSerializer(instance.post_comments.all(), many=True,
                                                                context=self.context).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        post = Post.objects.create(**validated_data)
        return post

    def get_likes(self, post):
        return Like.objects.filter(post=post).count()


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     validated_data['author_id'] = request.user
    #     comment = PostComment.objects.create(**validated_data)
    #     return comment
    #
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     # representation['author'] = UserSerializer(instance.author_id).data
    #     return representation


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id']

