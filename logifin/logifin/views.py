from django.shortcuts import render
import datetime

def hello(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})