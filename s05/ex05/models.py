from django.db import models


# To run create new table
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver
# 
# Create your models here.
class Movies(models.Model):
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self):
            return self.title
    class Meta:
          db_table = 'ex05_movies'