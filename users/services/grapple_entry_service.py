from typing import List

from django.db.models import Sum

from users.domain_models import Report
from users.models import GrappleEntry
from django.shortcuts import get_object_or_404


def fetch_all_grapple_entries_with_notes(user_id: int) -> List[GrappleEntry]:
    return [r for r in GrappleEntry.filter_by_user_has_notes(user_id)]


def generate_report(user_id: int) -> Report:
    grapple_entries = GrappleEntry.filter_by_user(user_id)
    
    #Numerical time display 
    total_hours_trained = (
        grapple_entries.aggregate(total_hours=Sum("hours_trained")).get("total_hours")
    )
    total_gi_entries = grapple_entries.filter(grappling_type="Gi")
    
    total_gi_hours = list(total_gi_entries.aggregate(gh=Sum("hours_trained")).values())[0]

    total_nogi_entries = grapple_entries.filter(grappling_type="Nogi")
    
    total_nogi_hours = (
        total_nogi_entries.aggregate(ngh=Sum("hours_trained"))["ngh"] or 0
    )
    
    total_minutes_trained = (
        grapple_entries.aggregate(total_minutes=Sum("minutes_trained")).get("total_minutes",0)
    )
    
    total_mat_time = int(round(total_hours_trained + (total_minutes_trained // 60)))


    
    
    
    # current_session_id = GrappleEntry.objects.get(id)
    return Report(
        grapple_entries=grapple_entries,
        hours_trained=total_hours_trained,
        minutes_trained=total_minutes_trained,
        total_mat_time=total_mat_time,
        all_gi_hours=total_gi_hours,
        all_nogi_hours=total_nogi_hours,
    )
