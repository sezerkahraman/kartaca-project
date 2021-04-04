import random
import time
from threading import Thread

from rest_framework import views
from rest_framework.response import Response

from common.helper import DateTimeHelper, RequestFileLogger


class RestAPIView(views.APIView):

    def _process_context(self, method):
        started_at = DateTimeHelper.get_current_millis()
        threshold = random.uniform(0, 3)
        time.sleep(threshold)
        finished_at = DateTimeHelper.get_current_millis()
        response_time = finished_at - started_at

        thread = Thread(target=RequestFileLogger.write_log_to_file,
                        args=(method, response_time))
        thread.start()
        thread.join()

    def get(self, request, *args, **kwargs):
        self._process_context(request.method)
        return Response('get metodu')

    def post(self, request, *args, **kwargs):
        self._process_context(request.method)
        return Response('post metodu')

    def put(self, request, *args, **kwargs):
        self._process_context(request.method)
        return Response('put metodu')

    def delete(self, request, *args, **kwargs):
        self._process_context(request.method)
        return Response('delete metodu')
