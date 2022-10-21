from rest_framework import serializers
from .models import Actor, Movie, Review

# 배우 전체
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

# 영화 타이틀만 
class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

# # 리뷰 타이틀, 내용만
# class ReviewTitleSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title','content',)

# 배우 상세
class ActorSerializer(serializers.ModelSerializer):
    movie_actors = MovieTitleSerializer(many = True)
    
    class Meta:
        model = Actor
        fields = '__all__'

# 배우 이름만
class ActorNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name',)

# 리뷰 전체
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

#  영화 상세
class MovieSerializer(serializers.ModelSerializer):
    # 배우 이름 보여주기
    actors = ActorNameSerializer(many=True)
    # 댓글 보여주기
    review_set = ReviewListSerializer(many=True)

    class Meta:
        model = Movie
        # exclude = ('actors',)
        fields = '__all__'
        # fields = ('title',)


# 영화 전체
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','overview',)



# 리뷰 상세 
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)