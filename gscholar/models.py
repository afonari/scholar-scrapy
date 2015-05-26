from django.db import models

class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization)
    coauthors = models.ManyToManyField("self")
    timestamp = models.DateField(auto_now=True)
#
class Organization(models.Model):
    email_domain = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
#