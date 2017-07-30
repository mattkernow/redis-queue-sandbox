from flask import Flask, request
from rq import Queue
from task import insert_into_db
from redis import Redis
from model import QueueObject
import logging
from datetime import datetime

app = Flask(__name__)

from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Create work queue
redis_conn = Redis()
q = Queue(connection=redis_conn)


@app.route('/add_to_queue/', methods=['POST', 'GET'])
def add_job_to_queue():
    """
    Enqueue task
    """
    content = request.get_json(force=True)
    content['added_to_queue'] = datetime.now()

    app.logger.info(content)

    queue_obj = QueueObject(content)

    # is_valid = queue_obj.validate()
    # app.logger.debug(is_valid)
    # if is_valid:
    queue_id = int(queue_obj.queue_id)
    date = str(queue_obj.added_to_queue)

    app.logger.info(date)

    q.enqueue(insert_into_db, queue_id, date)
    return '{} added to queue'.format(queue_id), 200
    # else:
    #     return "Bad input", 400

if __name__ == '__main__':
    app.run()