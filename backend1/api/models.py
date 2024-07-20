from django.db import models

# Create your models here.

from django.db import models
class Item(models.Model):
    firstname = models.CharField(max_length=100, default='')
    middlename = models.TextField(default='')
    lastname = models.TextField(default='')
    Address = models.TextField(default='')
    Barangay= models.TextField(default='')
    City= models.TextField(default='')
    State= models.TextField(default='')
    ZipCode= models.TextField(default='')
    Religion= models.TextField(default='')
    Sex= models.TextField(default='')
    Age= models.TextField(default='')
    Phone= models.TextField(default='')
    Email= models.TextField(default='')
    StudentID= models.TextField(default='')
    Height= models.TextField(default='')
    Weight= models.TextField(default='')
    Place_of_Birth = models.TextField(default='')
    Civil_Status= models.TextField(default='')
    Course= models.TextField(default='')
    Year= models.TextField(default='')
    Section= models.TextField(default='')
    Department= models.TextField(default='')
    Subject= models.TextField(default='')
    Citizenship= models.TextField(default='')
    School= models.TextField(default='')
    

    def __str__(self):
        return self.firstname