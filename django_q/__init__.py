from .tasks import async, schedule, result, fetch
from .models import Task, Schedule

VERSION = (0, 3, q)

default_app_config = 'django_q.apps.DjangoQConfig'
