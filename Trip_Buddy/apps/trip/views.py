from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from ..Login_Reg_App.models import *
from datetime import datetime


# Create your views here.
def trips(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": user,
        "trips": Trip.objects.all(), # all trips
        "my_trips": Trip.objects.filter(users_who_joined=user),
        "others": Trip.objects.exclude(users_who_joined=user)
    }
    return render(request, "trip/trips.html", context)

# if the tip creater is me then remove/edit. otherwise cancel


def new_trips(request):
    context = {
        "first_name": User.objects.get(id=request.session['user_id']).first_name
    }
    return render(request, "trip/new_trips.html", context)


def create(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/trips/new_trips")

    creator = User.objects.get(id=request.session['user_id'])
    my_trip = Trip.objects.create(
        destination=request.POST['destination'],
        plan=request.POST['plan'],
        start_date=request.POST['start_date'],
        end_date=request.POST['end_date'],
        creator=creator,
    )
    my_trip.users_who_joined.add(creator)
    return redirect("/trips")

def join(request, num):
    user = User.objects.get(id=request.session['user_id'])
    user.trips_joined.add(Trip.objects.get(id=num))
    return redirect("/trips")


def leave(request, num):
    user = User.objects.get(id=request.session['user_id'])
    user.trips_joined.remove(Trip.objects.get(id=num))
    return redirect("/trips")


def destroy(request, num):
    Trip.objects.get(id=num).delete()
    return redirect("/trips")

def edit_trip(request, num):
    context = {
        "trip": Trip.objects.get(id=num),
        "trip_start": datetime.strftime(Trip.objects.get(id=num).start_date, "%Y-%m-%d"),
        "trip_end": datetime.strftime(Trip.objects.get(id=num).end_date, "%Y-%m-%d"),
    }
    return render(request, "trip/edit_trips.html", context)


def update(request, num):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/trips/{num}/edit_trip")
    trip = Trip.objects.get(id=num)
    trip.destination = request.POST['destination']
    trip.plan = request.POST['plan']
    trip.start_date = request.POST['start_date']
    trip.end_date = request.POST['end_date']
    trip.save()
    return redirect("/trips")

def view_trip(request, num):
    trip = Trip.objects.get(id=num)
    context = {
        "trip": trip,
        "joiners": User.objects.filter(trips_joined=trip).exclude(id=trip.creator.id),
    }
    return render(request, "trip/view_trip.html", context)

