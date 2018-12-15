from django.db import models

# Create your models here.
from django.db import models


class CharityProject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    submitter = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lon = models.DecimalField(max_digits=8, decimal_places=3)
    submission_date = models.DateTimeField()
    stakeholder = models.ManyToManyField('CharityStakeholder', blank=True)
    bannerimage = models.ImageField(default='default.jpg', upload_to='project_pics')

    def __str__(self):
        return self.name


class CharityStakeholder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
