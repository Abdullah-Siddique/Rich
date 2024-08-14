from django.shortcuts import render
from datetime import datetime

def date_view(request):
    
    now = datetime.now()
    context = {
        'year': now.year,
        'month': now.month,
        'day': now.day,
    }
    
    return render(request, 'date/date_template.html', context)
# Create your views here.
