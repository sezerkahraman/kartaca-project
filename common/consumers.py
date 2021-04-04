from celery import shared_task
from kafka import KafkaConsumer

from common.enums import KafkaTopicNames
from common.helper import DateTimeHelper


def clean_value(value: bytes) -> str:
    return value.decode().strip('"').rstrip()


@shared_task
def consume_log_receiver():
    from common.models import RequestLog
    consumer = KafkaConsumer(KafkaTopicNames.REQUEST_LOGS.value,
                             bootstrap_servers=['kafka:19091'])
    for msg in consumer:
        values = clean_value(msg.value).split(',')
        RequestLog.objects.create(
            request_method=values[0],
            response_time=float(values[1]),
            request_timestamp=DateTimeHelper.timestamp_to_datetime(values[2]))

