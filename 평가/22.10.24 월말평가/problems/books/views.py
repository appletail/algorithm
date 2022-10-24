from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':  # 요청 방법 판단
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)  # 쿼리셋으로 가져오므로 many=True
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':  # 요청 방법 판단
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():  # 데이터 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 응답 상태코드


@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    book = get_object_or_404(Book, pk=book_pk)  # 조회대상 존재하지 않을때 404반환
    if request.method == 'GET':  # 요청 방법 판단
        serializer = BookSerializer(book)
        return Response(serializer.data)
    # Q 4.
    elif request.method == 'DELETE':  # 요청 방법 판단
        book.delete()
        data = {
            'delete': book_pk,  # 정상삭제시 반환할 data
        }
        return Response(data)
    # Q 5.
    elif request.method == 'PUT':  # 요청 방법 판단
        serializer = BookSerializer(book, data=request.data)  # 수정을 위한 serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    if request.method == 'GET':  # 요청 방법 판단
        Comments = Comment.objects.all()
        serializer = CommentSerializer(Comments, many=True)  # 쿼리셋으로 가져오므로 many=True
        return Response(serializer.data)



@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    if request.method == 'POST':  # 요청 방법 판단
        book = get_object_or_404(Book, pk=book_pk)  # 참조하는 게시글
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book)  # 참조하는 게시글 할당
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # Q 10.
    elif request.method == 'DELETE':  # 요청 방법 판단
        comment.delete()
        data = {
            'delete': comment_pk,  # 정상삭제시 반환할 data
        }
        return Response(data)