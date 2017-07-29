from flask import Flask, request
from rq import Queue
from task import insert_into_db
from redis import Redis
from model import QueueObject

app = Flask(__name__)

# Create work queue
redis_conn = Redis()
q = Queue(connection=redis_conn)


@app.route('/add_to_queue/', methods=['POST', 'GET'])
def add_job_to_queue():
    """
    Enqueue task
    """
    content = request.json
    queue_obj = QueueObject(content)
    queue_obj.validate()
    message = queue_obj.message
    q.enqueue(insert_into_db, message)
    return '{} added to queue'.format(content)
