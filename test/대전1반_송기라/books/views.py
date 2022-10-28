from functools import partial
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':
        # 객체 리스트 가져오기
        books = get_list_or_404(Book)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
        # json 형태로 반환 / 201 성공 응답 상태 코드
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # pk로 지정한 객체 가져오기
    book = get_object_or_404(Book, pk = book_pk)
    # Q 3.
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    # Q 4.
    elif request.method == 'DELETE':
        book.delete()
        # 204 삭제 성공 응답 상태 코드
        return Response(f'delete:{book_pk}', status=status.HTTP_204_NO_CONTENT)
    # Q 5.
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data, partial=True)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    # Q 7.
    if request.method == 'GET':
        # 객체 리스트 가져오기
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    if request.method == 'POST':
        # pk로 지정한 참조할 게시글 객체 가져오기
        book = get_object_or_404(Book, pk=book_pk)
        serializer = CommentSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save(book=book)
            # json 형태로 반환 / 201 성공 응답 상태 코드
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # pk로 지정한 객체 가져오기
    comment = get_object_or_404(Comment, pk=comment_pk)
    # Q 9.
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # Q 10.
    elif request.method == 'DELETE':
        comment.delete()
        return Response(f'delete : {comment_pk}')
