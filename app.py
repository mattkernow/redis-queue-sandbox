from flask import Flask, request
from rq import Queue
from task import insert_into_db
from redis import Redis
from model import RequestObject
from datetime import datetime

app = Flask(__name__)

# Create Redis connection and work queue
REDIS_CONNECTION = Redis()
REDIS_QUEUE = Queue(connection=REDIS_CONNECTION)


@app.route('/add_to_queue/', methods=['POST', 'GET'])
def add_job_to_queue():
    """
    Enqueue a task to update a timestamp column
    """
    # Record the time added to queue
    content = request.get_json(force=True)
    content['added_to_queue'] = datetime.now()

    # Create RequestObject instance
    # this validates the user input
    request_object = RequestObject(content)

    # Get the queue_id and datetime
    queue_id = int(request_object.queue_id)
    datetime_as_str = str(request_object.added_to_queue)

    # Add to Redis default queue
    REDIS_QUEUE.enqueue(insert_into_db, queue_id, datetime_as_str)
    return '{} added to queue'.format(queue_id), 200


if __name__ == '__main__':
    app.run()
