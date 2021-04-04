import json

from celery import shared_task
from django.conf import settings
from kafka import KafkaProducer

from common.enums import KafkaTopicNames


@shared_task
def consume_logs():
    producer = KafkaProducer(bootstrap_servers=['kafka:19091'],
                             value_serializer=lambda v: json.dumps(v).encode(
                                 'utf-8'))
    new_logs = []
    with open(settings.LOG_FILE_DIR, "r+") as f:
        print('before_truncate', 'settings_dir', settings.LOG_FILE_DIR)
        new_logs = f.read().splitlines()
        f.truncate(0)

    for log in new_logs:
        producer.send(topic=KafkaTopicNames.REQUEST_LOGS.value,
                      value=log)
