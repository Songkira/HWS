from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=50)
  genre = models.TextField(max_length=10)

  def __str__(self):

    return f'{self.id}번째 영화-{self.title}({self.genre})'

# .objects.all().order_by('id') # 오름차순
# .objects.all().order_by('-id') # 내림차순

# .objects.filter(title__startswith='')
# ~로 시작하는는 것만 조회
# .objects.filter(title__endswith='')
# ~로 끝나는 것만 조회
