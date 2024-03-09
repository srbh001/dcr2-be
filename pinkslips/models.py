import uuid
from django.db import models
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import now

# Create your models here.

class PinkSlip(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    student_name = models.CharField(max_length=200, default='')
    student_id = models.CharField(max_length=200, default='')
    date = models.DateField(default=now())
    # preferred_start_date = models.DateField(default=date.today())
    # preferred_end_date = models.DateField(default=date.today())
    reason = models.CharField(max_length=1000, blank=True, default='')
    approved = models.BooleanField(default=False, blank=True)
    
class Appointments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    student_name = models.CharField(max_length=200, default='')
    student_id = models.CharField(max_length=200, default='')
    preferred_start_date = models.DateField(default=now())
    preferred_end_date = models.DateField(default=now())
    reason = models.CharField(max_length=1000, blank=True, default='')
    approved = models.BooleanField(default=False, blank=True)
    assigned_date = models.DateField(default=now(), blank=True)

