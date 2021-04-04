import datetime

from django.views.generic.list import ListView
from rest_framework import viewsets, mixins

from common.helper import DateTimeHelper
from common.models import RequestLog
from common.resources.serializers import RequestLogSerializer


class RequestLogViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer


class RequestLogListView(ListView):
    template_name = 'report.html'
    queryset = RequestLog.objects.last_hour_requests()

    def get_context_data(self, **kwargs):
        context = super(RequestLogListView, self).get_context_data(**kwargs)
        for c in context['object_list']:
            c.request_timestamp = DateTimeHelper.get_milliseconds_from_datetime(
                c.request_timestamp)
        return context
