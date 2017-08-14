# Redis Python Queue System

1. start worker:

`rqworker &`

2. start Redis docker container:

`docker run --name python-redis -p 6379:6379 -d redis`

3. Run test class TestQueueSystem with nose or other test runner.

### Dashboard

Monitor the item proceed by the queue:

`rq-dashboard`

Runs on http://0.0.0.0:9181
