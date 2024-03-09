from django.db import models
from django.http import JsonResponse, HttpResponse
import re
from datetime import date
from random import *
import string

# Create your models here.

class PinkSlip(models.Model):
    student_name = models.CharField(max_length=200, default='')
    student_id = models.CharField(max_length=200, default='')
    date = models.DateField(default=date.today())
    # preferred_start_date = models.DateField(default=date.today())
    # preferred_end_date = models.DateField(default=date.today())
    pinkslip_id = models.CharField(max_length=200, default='')
    reason = models.CharField(max_length=1000, default='')
    approved = models.BooleanField(default=False)

    student_id = student_id.strip().upper()

    def __str__(self):
        return f'{self.student_name} - {self.student_id}'
    
class Appointments(models.Model):
    student_name = models.CharField(max_length=200, default='')
    student_id = models.CharField(max_length=200, default='')
    preferred_start_date = models.DateField(default=date.today())
    preferred_end_date = models.DateField(default=date.today())
    appointment_id = models.CharField(max_length=200, default='')
    reason = models.CharField(max_length=1000, default='')
    approved = models.BooleanField(default=False)
    assigned_date = models.DateField(default=None)

