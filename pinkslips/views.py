from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.decorators import api_view
from pinkslips.serializers import PinkSlipSerializer, AppointmentsSerializer
import random

@api_view(['GET'])
def search_pink_slip(request):
    if request.method == 'GET':
        if request.GET.get('pinkslip_id'):
            pink_slip = PinkSlip.objects.get(id=request.GET.get('pinkslip_id'))
            return JsonResponse({'pink_slip': pink_slip})
        
        pink_slips_data = []
        student_id = request.GET.get('student_id')
        pink_slips = PinkSlip.objects.all()
        for pink_slip in pink_slips:
            pink_slip_data = {
                'student_name': pink_slip.student_name,
                'student_id': pink_slip.student_id,
                'date': str(pink_slip.date),
                'pinkslip_id': pink_slip.pinkslip_id,
                'reason': pink_slip.reason,
                'approved': pink_slip.approved
            }
            pink_slips_data.append(pink_slip_data)
        return JsonResponse({'pink_slips': pink_slips_data})
    
    else:
        return JsonResponse({'error': 'Unsupported request method'}, status=405)

@api_view(['POST'])
def create_pink_slip(request):
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
            pinkslip_id="".join([random.choice(string.ascii_letters + string.digits) for i in range(randint(8, 16))]),
            approved=False
        )

        return JsonResponse({'pink_slip': pink_slip})

@api_view(['GET'])
def search_appointment(request):
    if request.method == 'GET':
        if request.GET.get('appointment_id'):
            appointment = Appointments.objects.get(id=request.GET.get('appointment_id'))
            return JsonResponse({'appointment': appointment})
        
        appointments_data = []
        student_id = request.GET.get('student_id')
        appointments = Appointments.objects.filter(student_id=student_id)
        for appointment in appointments:
            appointment_data = {
                'student_name': appointment.student_name,
                'student_id': appointment.student_id,
                'preferred_start_date': str(appointment.preferred_start_date),
                'preferred_end_date': str(appointment.preferred_end_date),
                'appointment_id': appointment.appointment_id,
                'reason': appointment.reason,
                'approved': appointment.approved,
                'assigned_date': appointment.assigned_date
            }
            appointments.append(appointment_data)
        serialized_data = AppointmentsSerializer(appointments, many=True)
        return JsonResponse({'appointments': serialized_data.data})
    
    else:
        return JsonResponse({'error': 'Unsupported request method'}, status=405)

@api_view(['POST'])
def create_appointment(request):
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
            appointment_id="".join([random.choice(string.ascii_letters + string.digits) for i in range(randint(8, 16))]),
            approved=False,
            assigned_date=None
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