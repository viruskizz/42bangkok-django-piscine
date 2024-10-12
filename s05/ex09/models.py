from django.db import models


# To run create new table
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver
# 
# Create your models here.
class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(null=True)
    diameter = models.PositiveIntegerField(null=True)
    orbital_period = models.PositiveIntegerField(null=True)
    population = models.PositiveBigIntegerField(null=True)
    rotation_period = models.PositiveIntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'ex09_planets'

class People(models.Model):
    name = models.CharField(max_length=64, null=False)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.PositiveIntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(
        Planets,
        null=True,
        on_delete=models.SET_NULL,
        db_column='homeworld',
        related_name="planet",
        db_constraint=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'ex09_people'
