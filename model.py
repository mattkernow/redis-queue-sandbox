import datetime
from schematics.models import Model
from schematics.types import StringType, DateTimeType, IntType


class QueueObject(Model):
    queue_id = IntType()
    added_to_queue = DateTimeType(default=datetime.datetime.now)
