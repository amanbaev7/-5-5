from .models import Article, Comment
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    article_id = serializers.IntegerField(write_only=True, source='article')
    
    class Meta:
        model = Comment
        fields = ['id', 'article', 'article_id', 'username', 'message', 'likes', 'created_at']
        read_only_fields = ['id', 'likes', 'created_at']
    
    def validate_message(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Message cannot be empty")
        return value
        
        
