from rest_framework import serializers
from pinkslips.models import PinkSlip, Appointments

class PinkSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinkSlip
        fields = '__all__'

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'
    