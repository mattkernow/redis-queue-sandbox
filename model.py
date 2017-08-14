import datetime
from schematics.models import Model
from schematics.types import DateTimeType, IntType


class RequestObject(Model):
    """
    Model for request
    """
    queue_id = IntType()
    added_to_queue = DateTimeType(default=datetime.datetime.now)
