from django.db.models import Sum

from users.domain_models import Report
from users.models import GrappleEntry


def generate_report(user_id: int) -> Report:
    grapple_entries = GrappleEntry.objects.filter(user_id=user_id)
    total_hours_trained = (
        grapple_entries.aggregate(
            total_hours=Sum("hours_trained")
        )["total_hours"]
        or 0
    )

    total_minutes_trained = (
        grapple_entries.aggregate(
            total_minutes=Sum("minutes_trained")
        )["total_minutes"]
        or 0
    )

    total_mat_time = round(total_hours_trained + (total_minutes_trained // 60))

    return Report(
        grapple_entries=grapple_entries,
        hours_trained=total_hours_trained,
        minutes_trained=total_minutes_trained,
        total_mat_time=total_mat_time
    )
