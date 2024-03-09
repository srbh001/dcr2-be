from django.db import models
from django.http import JsonResponse, HttpResponse
import re
from datetime import date
from random import *
import string
from django.utils.timezone import now

# Create your models here.

class PinkSlip(models.Model):
    student_name = models.CharField(max_length=200, default='')
    student_id = models.CharField(max_length=200, default='')
    date = models.DateField(default=now())
    # preferred_start_date = models.DateField(default=date.today())
    # preferred_end_date = models.DateField(default=date.today())
    pinkslip_id = models.CharField(max_length=200, blank=True, default='')
    reason = models.CharField(max_length=1000, blank=True, default='')
    approved = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.student_name} - {self.student_id}'
    
class Appointments(models.Model):
    student_name = models.CharField(max_length=200, default='')
    student_id = models.CharField(max_length=200, default='')
    preferred_start_date = models.DateField(default=now())
    preferred_end_date = models.DateField(default=now())
    appointment_id = models.CharField(max_length=200, blank=True, default='')
    reason = models.CharField(max_length=1000, blank=True, default='')
    approved = models.BooleanField(default=False, blank=True)
    assigned_date = models.DateField(default=now(), blank=True)

