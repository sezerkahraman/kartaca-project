import datetime
from datetime import timedelta

from django.db.models import QuerySet


class RequestLogQuerySet(QuerySet):

    def last_hour_requests(self):
        last_hour_date_time = datetime.datetime.now() - timedelta(hours=1)
        return self.filter(request_timestamp__gte=last_hour_date_time)

