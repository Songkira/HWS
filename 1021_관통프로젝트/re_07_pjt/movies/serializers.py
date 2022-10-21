from .models import Actor, Movie, Review
from rest_framework import serializers

# 배우 전체
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

# 영화 제목만
class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

# 배우 상세        
class ActorSerializer(serializers.ModelSerializer):
    movie_actors = MovieTitleSerializer(many = True)
    
    class Meta:
        model = Actor
        fields = '__all__'
        
# 영화 전체
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

# 배우 이름만
class ActorNameSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name', )

# 리뷰 전체
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

# 영화 상세
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSeralizer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


# 리뷰 상세
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
