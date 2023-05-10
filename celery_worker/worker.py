import os
from celery import Celery
from kombu import Queue

BROKER_URI = os.environ['BROKER_URI']
BACKEND_URI = os.environ['BACKEND_URI']

celery_app = Celery(
    'celery_worker',
    broker=BROKER_URI,
    backend=BACKEND_URI,
    include=['celery_worker.tasks', 'celery_worker.ml.model'],
    worker_prefetch_multiplier=1
)
#
# celery_app.conf.task_queues = (
#     Queue('PendingMeetingQueue', routing_key='PendingMeetingQueue'),
#     Queue('InProcessMeetingQueue', routing_key='InProcessMeetingQueue'),
#     Queue('ReadyMeetingQueue', routing_key='ReadyMeetingQueue'),
# )
# celery_app.conf.task_routes = {
#     'celery_worker.summarize_meeting': {'queue': 'PendingMeetingQueue'},
#     'celery_worker.process_meeting': {'queue': 'InProcessMeetingQueue'},
#     'celery_worker.finish_meeting': {'queue': 'ReadyMeetingQueue'},
# }