from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Value, F
#from datetime import datetime, timedelta, weekday
import datetime
from accounts.models import *


# Create your views here.
@login_required
def dashboard(request):
    worked_hours_week = 0#34
    worked_hours_total = 0#215
    completed_task = 0#30

    #suma de horas trabajadas por el request.user
    time_intervals = TimeInterval.objects.filter(user=request.user)#.aggregate(a=Sum((timeinterval.end_time.hour-timeinterval.init_time.hour)))
    for i in time_intervals:
        worked_hours_total = worked_hours_total + hours(i.end_time, i.init_time)#(i.end_time.datetime - i.init_time.datetime).hour


    # El intervalo entre start_date y end_date es de lunes a viernes
    today = datetime.datetime.today()
    day_of_week = today.weekday()
    start_date = today - datetime.timedelta(days=day_of_week)
    end_date = start_date + datetime.timedelta(days=4)
    st = start_date.time
    et = end_date.time
    time_intervals = TimeInterval.objects.filter(user=request.user, end_time__lte=et,  init_time__gte=st)

    for i in time_intervals:
        worked_hours_week = worked_hours_week + hours(i.end_time, i.init_time)#(i.end_time.datetime - i.init_time.datetime).hour

    completed_task = Task.objects.filter(status='Closed', usertaskassignrelation__user=request.user).count()

    args = {'worked_hours_week': worked_hours_week, 
            'worked_hours_total': worked_hours_total, 
            'completed_task': completed_task }

    return render(request, 'home.html', args)

def hours(end_hour, start_hour):
    end_minutes = end_hour.hour*60 + end_hour.minute
    start_minutes = start_hour.hour*60 + start_hour.minute
    return (end_minutes - start_minutes) #// 60

@login_required
def vacaciones(request):
    return render(request,'solicitud_vacaciones.html',{'variable':''})

@login_required
def adelanto(request):
    return render(request,'solicitud_adelanto.html',{'variable':''})

@login_required
def consulta_horas_trabajadas(request):
    return render(request,'consulta_horas.html',{'variable':''})

@login_required
def registro_horas_trabajadas(request):
    return render(request,'registro_horas.html',{'variable':''})

@login_required
def reporte(request):
    return render(request,'reporte_faltas.html',{'variable':''})

@login_required
def tareas(request):
    return render(request,'tareas.html',{'variable':''})