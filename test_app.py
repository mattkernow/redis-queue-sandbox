import unittest
from app import app


class TestQueueSystem(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_add_item_to_queue(self):
        queue_id = '3'
        payload = '{"queue_id": %s}' % queue_id

        rv = self.app.post('/add_to_queue/',
                                      content_type='application/json',
                                      data=payload)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, b'3 added to queue')

if __name__ == '__main__':
    unittest.main()
