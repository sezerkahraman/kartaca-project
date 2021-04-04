from django.db import models

from common.managers import RequestLogQuerySet


class RequestLog(models.Model):
    request_method = models.CharField(max_length=15)
    request_timestamp = models.DateTimeField(db_index=True)
    response_time = models.BigIntegerField()

    objects = RequestLogQuerySet.as_manager()
