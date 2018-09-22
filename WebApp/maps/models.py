from django.db import models

# Create your models here.

#Model to store the search history
class MyWayPointsData(models.Model):
    start_point = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    search_date = models.DateField('Date Searched')

