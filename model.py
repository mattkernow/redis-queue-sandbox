import datetime
from schematics.models import Model
from schematics.types import DateTimeType, IntType


class QueueObject(Model):
    """
    Model for queue item update
    """
    queue_id = IntType()
    added_to_queue = DateTimeType(default=datetime.datetime.now)
