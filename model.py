import datetime
from schematics.models import Model
from schematics.types import StringType, DateTimeType, IntType


class QueueObject(Model):
    message = StringType()
    added_to_queue = DateTimeType(default=datetime.datetime.now)
