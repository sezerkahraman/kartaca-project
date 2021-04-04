from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from common.resources.views import RequestLogViewSet, RequestLogListView

_router = routers.DefaultRouter()
_router.register(r'request-logs', RequestLogViewSet, "request-logs")

urlpatterns = [
    url(r'^',
        include((_router.urls, 'request-logs'), namespace='request-logs')),
    path('report', RequestLogListView.as_view(), name='request-log-list'),
]
