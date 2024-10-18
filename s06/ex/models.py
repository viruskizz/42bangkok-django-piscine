from django.db import models

# Create your models here.
from django.db import models

# To run create new table
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver
# 
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
