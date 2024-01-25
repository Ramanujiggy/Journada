from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse
from .models import Profile, GrappleEntry
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django import forms
from .forms import TrainingSessionForm
import json


def index(request):  # returns all users
    all_users = Profile.objects.all()
    data = serialize("json", all_users, fields=("username", "user_email"))
    return HttpResponse(data, content_type="application/json")


def search(request, user_id):  # retrieve a specific user
    try:
        user = Profile.objects.get(pk=user_id)
        serialized_data = serialize("json", [user], fields=("username", "user_email"))
        return HttpResponse(serialized_data)
    except Profile.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


def log_session(request):
    form = TrainingSessionForm
    if request.method == "POST":
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            training_session = form.save(commit=False)
            training_session.user = request.user
            hours_trained = form.cleaned_data["hours_trained"]
            minutes_trained = form.cleaned_data["minutes_trained"]
            grappling_type = form.cleaned_data["grappling_type"]
            date = form.cleaned_data["date"]
            hours = form.cleaned_data["time"]
            training_session.save()
            return redirect(
                "home"
            )  # change this to the dashboard view for triaining sessions
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = TrainingSessionForm()
    return render(request, "create_training_log.html", {"form": form})


@login_required
def dashboard(request):
    """returns all training sessions for specific user"""
    user = get_user(request)
    user_id = user.id
    sessions = GrappleEntry.objects.filter(user=user)
    total_hours_trained = (
        GrappleEntry.objects.filter(id=user_id).aggregate(
            total_hours=Sum("hours_trained")
        )["total_hours"]
        or 0
    )

    total_minutes_trained = (
        GrappleEntry.objects.filter(id=user_id).aggregate(
            total_minutes=Sum("minutes_trained")
        )["total_minutes"]
        or 0
    )

    if total_minutes_trained >= 60:
        total_hours_trained += total_minutes_trained // 60
        total_mat_time = total_hours_trained

    else:
        total_mat_time = float(round(total_hours_trained + total_minutes_trained))

    return render(
        request,
        "view_training_logs.html",
        {
            "sessions": sessions,
            "hours_trained": total_hours_trained,
            "minutes_trained": total_minutes_trained,
            "total_mat_time": round(total_mat_time),
        },
    )


"""
    hours_trained = (
        GrappleEntry.objects.filter(user=request.user).aggregate(Sum("hours_trained"))[
            "hours_trained"
        ]
        or 0
    )

    minutes_trained = GrappleEntry.objects.filter(user=request.user).aggregate(
        Sum("minutes_trained")
    )["minutes_trained"]
    if minutes_trained >= 60:
        hours_trained += minutes_trained // 60
        total_mat_time = hours_trained

    else:
        total_mat_time = hours_trained + minutes_trained
"""
