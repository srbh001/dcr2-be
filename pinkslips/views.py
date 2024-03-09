from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import string
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pinkslips.serializers import PinkSlipSerializer, AppointmentsSerializer, InventoryItemSerializer, BillingSerializer
import random

@api_view(['GET'])
def pinkslip(request, id):
    if request.method == 'GET':
        if id:
            pink_slip = PinkSlip.objects.filter(id=id).first()
            return JsonResponse({'pink_slip': pink_slip})
        
        # pink_slips_data = []
        # student_id = request.GET.get('student_id')
        # pink_slips = PinkSlip.objects.all()
        # for pink_slip in pink_slips:
        #     pink_slip_data = {
        #         'student_name': pink_slip.student_name,
        #         'student_id': pink_slip.student_id,
        #         'date': str(pink_slip.date),
        #         'id': pink_slip.id,
        #         'reason': pink_slip.reason,
        #         'approved': pink_slip.approved
        #     }
        #     pink_slips_data.append(pink_slip_data)
        # return JsonResponse({'pink_slips': pink_slips_data})
    
    else:
        return JsonResponse({'error': 'Unsupported request method'}, status=405)

@api_view(['GET', 'POST'])
def pinkslips(request):
    if request.method == 'GET':
        pink_slips_data = []
        pink_slips = PinkSlip.objects.all()
        for pink_slip in pink_slips:
            pink_slip_data = {
                'student_name': pink_slip.student_name,
                'student_id': pink_slip.student_id,
                'date': str(pink_slip.date),
                'id': pink_slip.id,
                'reason': pink_slip.reason,
                'approved': pink_slip.approved
            }
            pink_slips_data.append(pink_slip_data)
        
        serialized_data = PinkSlipSerializer(pink_slips, many=True)
        return JsonResponse({'pink_slips': serialized_data.data})
    
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        date = request.POST.get('date')
        # preferred_start_date = request.POST.get('preferred_start_date')
        # preferred_end_date = request.POST.get('preferred_end_date')
        reason = request.POST.get('reason')

        # if len(student_id.strip()) < 7 or re.match(r'^((2[23][BbMm][0-9]{4})|([0-9]{9}))$', student_id.strip()) is None:
        #     raise ValueError('Student ID not correct')
        # if preferred_end_date < preferred_start_date:
        #     raise ValueError('End date cannot be before start date')
        # if preferred_start_date <  date.today():
        #     raise ValueError('Start date cannot be before today')

        pink_slip = PinkSlip.objects.create(
            student_name=student_name,
            student_id=student_id,
            date=date,
            # preferred_start_date=preferred_start_date,
            # preferred_end_date=preferred_end_date,
            reason=reason,
            id=id,
            approved=False
        )

        return JsonResponse({'pink_slip': pink_slip})

@api_view(['GET'])
def appointment(request, id):
    if request.method == 'GET':
        if id:
            pink_slip = Appointments.objects.filter(id=id).first()
            return JsonResponse({'pink_slip': pink_slip})

        # appointments_data = []
        # student_id = request.GET.get('student_id')
        # # appointments = Appointments.objects.filter(student_id=student_id)
        # appointments = Appointments.objects.all()
        # for appointment in appointments:
        #     appointment_data = {
        #         'student_name': appointment.student_name,
        #         'student_id': appointment.student_id,
        #         'preferred_start_date': str(appointment.preferred_start_date),
        #         'preferred_end_date': str(appointment.preferred_end_date),
        #         'appointment_id': appointment.id,
        #         'reason': appointment.reason,
        #         'approved': appointment.approved,
        #         'assigned_date': appointment.assigned_date
        #     }
        #     appointments_data.append(appointment_data)
        # serialized_data = AppointmentsSerializer(appointments, many=True)
        # return JsonResponse({'appointments': serialized_data.data})
    
    else:
        return JsonResponse({'error': 'Unsupported request method'}, status=405)

@api_view(['GET', 'POST'])
def appointments(request):
    if request.method == 'GET':
        appointments_data = []
        # student_id = request.GET.get('student_id')
        appointments = Appointments.objects.all()
        for appointment in appointments:
            appointment_data = {
                'student_name': appointment.student_name,
                'student_id': appointment.student_id,
                'preferred_start_date': str(appointment.preferred_start_date),
                'preferred_end_date': str(appointment.preferred_end_date),
                'appointment_id': appointment.id,
                'reason': appointment.reason,
                'approved': appointment.approved,
                'assigned_date': appointment.assigned_date
            }
            appointments_data.append(appointment_data)

        serialized_data = AppointmentsSerializer(appointments, many=True)
        return JsonResponse({'appointments': serialized_data.data})
    
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        # date = request.POST.get('date')
        preferred_start_date = request.POST.get('preferred_start_date')
        preferred_end_date = request.POST.get('preferred_end_date')
        reason = request.POST.get('reason')

        new_name = str(student_name)
        # if len(student_id) < 7 or re.match(r'^((2[23][BbMm][0-9]{4})|([0-9]{9}))$', student_id.strip()) is None:
        #     raise ValueError('Student ID not correct')
        # if preferred_end_date < preferred_start_date:
        #     raise ValueError('End date cannot be before start date')
        # if preferred_start_date <  date.today():
        #     raise ValueError('Start date cannot be before today')

        appointment = Appointments.objects.create(
            student_name=student_name,
            student_id=student_id,
            # date=date,
            preferred_start_date=preferred_start_date,
            preferred_end_date=preferred_end_date,
            reason=reason,
            appointment_id=id,
            approved=False,
            assigned_date=now()
        )

        serialized_data = AppointmentsSerializer(appointment, many=True)
        return JsonResponse({'appointment': serialized_data.data})

def approve_reject_pinkslip(request):
    if request.method == 'POST':
        pink_slip = PinkSlip.objects.get(id=request.POST.get('pinkslip_id'))
        pink_slip.approved = request.POST.get('approved')
        pink_slip.save()
        return JsonResponse({'pink_slip': pink_slip})

def approve_reject_pinkslip(request):
    if request.method == 'POST':
        pink_slip = PinkSlip.objects.get(id=request.POST.get('pinkslip_id'))
        pink_slip.approved = request.POST.get('approved')
        pink_slip.save()
        return JsonResponse({'pink_slip': pink_slip})

@api_view(['GET', 'POST'])
def inventory_list(request):
    if request.method == 'GET':
        inventory = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(inventory, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def inventory_detail(request, pk):
    try:
        inventory = InventoryItem.objects.get(pk=pk)
    except InventoryItem.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = InventoryItemSerializer(inventory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InventoryItemSerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        inventory.delete()
        return Response(status=204)
    
@api_view(['GET', 'POST'])
def billing_list(request):
    if request.method == 'GET':
        billing = Billing.objects.all()
        serializer = BillingSerializer(billing, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BillingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def billing_detail(request, pk):
    try:
        billing = Billing.objects.get(pk=pk)
    except Billing.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BillingSerializer(billing)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BillingSerializer(billing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        billing.delete()
        return Response(status=204)
