from django.db import models
import uuid
from django.conf import settings


# Create your models here.


class Movie(models.Model):

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('derama', 'Derama'),
        ('horror', 'Horror'),
        ('remance', 'Remance'),
        ('science_fiction', 'Science_fiction'),
        ('fantasy', 'Fantasy'),


    ]
    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=100)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_caver = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
