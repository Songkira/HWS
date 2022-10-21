from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import ActorSerializer, ActorListSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from . models import Actor, Movie, Review
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def actor_list(request):
    acotrs = Actor.objects.all()
    serializer = ActorListSerializer(acotrs, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    acotr = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(acotr)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many = True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        res = {'msg':f'{review_pk} 번 리뷰 삭제'}
        return Response(res, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



