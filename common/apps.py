import sys

from django.apps import AppConfig

from common.consumers import consume_log_receiver


class CommonConfig(AppConfig):
    name = 'common'

    def ready(self):
        # TODO: try this in urls.py
        #  https://stackoverflow.com/a/63060317/7659834
        if 'runserver' in sys.argv:
            consume_log_receiver.delay()

