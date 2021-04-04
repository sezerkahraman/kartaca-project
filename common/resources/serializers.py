from rest_framework import serializers

from common.models import RequestLog


class RequestLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestLog
        fields = '__all__'
