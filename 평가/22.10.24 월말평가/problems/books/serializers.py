from rest_framework import serializers
from .models import Book, Comment


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):
    # Q 6.
    book = BookListSerializer(read_only=True)  # 댓글이 참조하고 있는 게시글 / read_only를 줘서 게시글 생성 유효성 검사에서 제외시킴
    class Meta:
        model = Comment
        fields = '__all__'  # 모든 필드

class BookSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    # Q 11.
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('comment_count',)