from typing import Iterable

from users.models import GrappleEntry


class Report:
    def __init__(
        self,
        grapple_entries: Iterable[GrappleEntry],
        hours_trained: float,
        minutes_trained: float,
        total_mat_time: float,
        all_gi_hours: str,
        all_nogi_hours: str,
    ):
        self.grapple_entries = grapple_entries
        self.minutes_trained = minutes_trained
        self.hours_trained = hours_trained
        self.total_mat_time = (total_mat_time,)
        self.all_gi_hours = (all_gi_hours,)
        self.all_nogi_hours = all_nogi_hours
