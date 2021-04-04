from django.urls import path

from .views import RestAPIView
from common.urls import urlpatterns as common_urls

urlpatterns = [
    path('', RestAPIView.as_view()),
]

urlpatterns += common_urls
