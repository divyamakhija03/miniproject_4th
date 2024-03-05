import json
from django.shortcuts import render
from django.db.models import Count
from complaintApp.models import Griv

# Create your views here.
def adminhome(request):
    gender_data = Griv.objects.values('gender').annotate(count=Count('id'))
    resolution_data = Griv.objects.values('preferred_resolution').annotate(count=Count('id'))
    status_data = Griv.objects.values('status').annotate(count=Count('id'))

    print('Gender Data:', list(gender_data))
    print('Resolution Data:', list(resolution_data))
    print('Status Data:', list(status_data))
    
    context = {
        'gender_data': json.dumps(list(gender_data),safe=False),
        'resolution_data': json.dumps(list(resolution_data),safe=False),
        'status_data': json.dumps(list(status_data),safe=False)
    }
    return render(request,'adminHome/home.html',context)


# Create your views here.
# in views.py (sixth app)






