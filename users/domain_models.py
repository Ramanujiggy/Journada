from typing import Iterable

from users.models import GrappleEntry


class Report:
    def __init__(
            self,
            grapple_entries: Iterable[GrappleEntry],
            hours_trained: float,
            minutes_trained: float,
            total_mat_time: float
    ):
        self.grapple_entries = grapple_entries
        self.minutes_trained = minutes_trained
        self.hours_trained = hours_trained
        self.total_mat_time = total_mat_time
