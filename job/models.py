from datetime import *
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator, MaxValueValidator

class JobType(models.TextChoices):
    Fulltime = 'Full Time'
    Temporary = 'Temporary'
    Intership = 'Intership'

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'

class Industry(models. TextChoices):
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education/Training'
    Telecommunication = 'Telecommunication'
    Others = 'Others'

class Experience(models. TextChoices):
    NO_EXPERIENCE = 'No Experience'
    ONE_YEAR = '1 Years'
    TWO_YEAR = '2 Years'
    THREE_YEAR_PLUS = '3 Years above'

def return_date_time():
    now = datetime.now()
    return now + timedelta(days=30)

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType= models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.Fulltime
    )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models. CharField(
        max_length=30,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models. CharField(
        max_length=20,
        choices=Experience. choices,
        default=Experience.NO_EXPERIENCE
    )
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    positions = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0,0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    
class CandidatesApplied(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resume = models.CharField(max_length=200)
    appliedAt = models.DateTimeField(auto_now_add=True)
