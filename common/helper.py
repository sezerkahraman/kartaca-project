import datetime
import time
from typing import Union

from django.conf import settings


class DateTimeHelper:
    @staticmethod
    def get_current_millis():
        return round(time.time() * 1000)

    @staticmethod
    def timestamp_to_datetime(timestamp_value: Union[str, int]) -> datetime:
        return datetime.datetime.fromtimestamp(int(timestamp_value) / 1000.0)

    @staticmethod
    def get_milliseconds_from_datetime(datetime_value: datetime) -> float:
        return datetime_value.timestamp() * 1000


class RequestFileLogger:
    @staticmethod
    def write_log_to_file(method_type: str,
                          response_time: float):
        timestamp = DateTimeHelper.get_current_millis()
        with open(settings.LOG_FILE_DIR, "a") as f:
            f.write(f"{method_type},{response_time},{timestamp}\n")
            f.close()
