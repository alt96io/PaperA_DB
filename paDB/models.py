from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    #NEW REPORT AUTO CREATES SECTION AND SETS USER TO CREATOR
    REPORT_STATUS_CHOICES = (
        ('draft','Draft'),
        ('submitted','Submitted'),
        ('deleted','Deleted'),
    )
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    status = models.CharField(max_length=50, choices = REPORT_STATUS_CHOICES)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    report = models.ForeignKey(Report, on_delete=models.SET_NULL,null=True,blank=True)

# How section info returns when queried
    def __str__(self):
        return self.title


class Content(models.Model):
    CONTENT_STATUS_CHOICES = (
        ('proposed','Proposed'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )
    content_str = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices = CONTENT_STATUS_CHOICES)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.content_str

class ReportDiscussion(models.Model):
    post = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    # Report should have cascading on delete********
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return self.post

class Roles(models.Model):
    # USE GROUPS IN DJANGOADMIN TO SEPARATE CLIENTS IN MVP
    # Maybe we use roles in Django (e.g. Admin, staff, user)
    role = models.CharField(max_length=1000)

    def __str__(self):
        return self.role

class UserRole(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL,null=True,blank=True)

class UserRoleSection(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL,null=True,blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,null=True,blank=True)
