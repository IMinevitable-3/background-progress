from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .tasks import start_new_job


class StartNewJob(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        new_celery_task = start_new_job.delay()
        return Response(
            data={
                "result": "Job created",
                "celery_task_id": new_celery_task.id,
            },
            status=status.HTTP_200_OK,
        )
