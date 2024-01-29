from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .forms import TrainingSessionForm

from .services import report_generator


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
            return redirect("/users/dashboard")
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

    report = report_generator.generate_report(user_id=user_id)

    return render(
        request,
        "view_training_logs.html",
        {
            "sessions": report.grapple_entries,
            "hours_trained": report.hours_trained,
            "minutes_trained": report.minutes_trained,
            "total_mat_time": report.total_mat_time,
        },
    )
