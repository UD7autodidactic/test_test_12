from types import MemberDescriptorType
from django.db import models 
from datetime import datetime , date, timezone
from django.forms import DateTimeField, TimeField 
from datetime import time

class Courses_detail(models.Model):
    course_list = models.CharField(max_length=100 ,blank=True , null =True)
    course_fee = models.IntegerField(blank=True , null =True )
    course_time =  models.CharField(max_length=50); 
    # int_field = models.IntegerField()
    course_time_2 =  models.CharField(max_length=50); 
    # int_field = models.IntegerField()
    instructor = models.CharField(max_length=100)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    school_name = models.CharField(max_length=50)
    parents_occupation = models.CharField(max_length=100)
    courses = models.ManyToManyField(Courses_detail , max_length=4)
    fees = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True)
    timestamp = models.DateField(auto_now_add=True) 

class UsCoursesDetail(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses_detail,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('member', 'course')

