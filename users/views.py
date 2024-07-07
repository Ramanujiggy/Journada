from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, GrappleEntry
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .forms import TrainingSessionForm
from django.shortcuts import get_object_or_404

from users.services import grapple_entry_service


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


def list_journal_notes(request):
    user = get_user(request)
    user_id = user.id
    grapple_entries = grapple_entry_service.fetch_all_grapple_entries_with_notes(
        user_id
    )
    report = grapple_entry_service.generate_report(user_id=user_id) 
    
    return render(
        request, "view_journal_notes.html",
        {
        "grapple_entries": grapple_entries,
        "sessions": report.grapple_entries,
        }
    )


def log_session(request):
    form = TrainingSessionForm
    if request.method == "POST":
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            training_session = form.save(commit=False)
            training_session.user = request.user
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

    report = grapple_entry_service.generate_report(user_id=user_id)
    
    return render(
        request,
        "view_training_logs.html",
        {
            "hours_trained": report.hours_trained,
            "minutes_trained": report.minutes_trained,
            "total_mat_time": report.total_mat_time,
            "gi_hours": report.all_gi_hours,
            "nogi_hours": report.all_nogi_hours,
            "sessions": report.grapple_entries,
        }
    )


@login_required
def edit_grapple_entry(request, grapple_entry_id):
    """allows user to edit grapple_entry"""
    user = request.user
    current_entry = get_object_or_404(GrappleEntry, pk=grapple_entry_id, user=user)

    if request.method == "POST":
        form = TrainingSessionForm(request.POST, instance=current_entry)
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("users:dashboard")
    else:
        print("form is invalid")
        print(TrainingSessionForm.__dict__)
        form = TrainingSessionForm(instance=current_entry)

    return render(
        request,
        "edit_training_log.html",
        {
            "form": form,
            "hours_trained": current_entry.hours_trained,
            "minutes_trained": current_entry.minutes_trained,
            "grappling_type": current_entry.grappling_type,
            "date": current_entry.date.strftime("%Y-%m-%d"),
            "time": current_entry.time.strftime("%H-%M-%S"),
            "notes": current_entry.notes,
        },
    )

        # write out code to validate that the data was entered into the database and if valid a toast message is generated
        #this could be done with ajax? but look into if Django has this functionality as well. 