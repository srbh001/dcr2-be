from rest_framework import serializers
from pinkslips.models import PinkSlip, Appointments, InventoryItem, Billing



class PinkSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinkSlip
        fields = '__all__'

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'
InventoryItemSerializer, BillingSerializer