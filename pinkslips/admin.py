from django.contrib import admin

# Register your models here.
from pinkslips.models import PinkSlip, Appointments


admin.site.register(PinkSlip)
admin.site.register(Appointments)
