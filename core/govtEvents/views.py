from django.shortcuts import render,redirect
from .models import events

# Create your views here.
def eventPage(request):
    eventsData = events.objects.all()
    print(eventsData)
    return render(request,'govtEvents/events.html',context={'governmentEvents':eventsData})


def addEvent(request):
    if request.method == "POST":
        event_name = request.POST['eventName']
        event_description = request.POST['eventDescription']
        event_date = request.POST['eventDate']
        event_contact = request.POST['eventContact']
        en = events(event_name=event_name,event_description=event_description,event_date=event_date,event_contact=event_contact)
        en.save()
    return redirect("http://localhost:8000/govtEvents/eventPage/")