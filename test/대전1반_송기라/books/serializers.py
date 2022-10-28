from rest_framework import serializers
from .models import Book, Comment


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):
    # Q 6.
    class Meta:
        model = Comment
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # Q 11.
    # 댓글의 수를 직렬화
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
