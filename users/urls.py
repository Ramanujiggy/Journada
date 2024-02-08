from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("log_session", views.log_session, name="log_session"),
    path("journal_entries", views.list_journal_notes, name="list_journal_notes"),
    path("edit_grapple_entry/<int:grapple_entry_id>/",views.edit_grapple_entry,name="edit_grapple_entry",
    )
]
