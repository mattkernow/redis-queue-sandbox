import unittest
from app import app
import psycopg2
from task import DB_CONNECTION


def execute_query(query_str, num_of_runs=1):
    conn = psycopg2.connect(DB_CONNECTION)
    cur = conn.cursor()

    for new_row in range(num_of_runs):
        cur.execute(query_str)
    conn.commit()

    try:
        return cur.fetchall()
    except psycopg2.ProgrammingError:
        return


class TestQueueSystem(unittest.TestCase):

    # Set True to not truncate after test
    TRUNCATE_AFTER_TEST = False

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        if self.TRUNCATE_AFTER_TEST is True:
            execute_query('TRUNCATE TABLE public.migration_id;')

    def test_add_item_to_queue_batch(self):
        # Arrange
        items_to_queue = 2000

        # Act
        for row in range(items_to_queue):

            payload = '{"queue_id": %s}' % row
            response = self.app.post('/add_to_queue/',
                                     content_type='application/json',
                                     data=payload)

            # Assert
            self.assertEqual(response.status_code, 200)

    def test_add_item_to_queue_reject_non_integer_input(self):
        # Arrange
        str_type_object = 'i am a string, the api expects integer'
        payload = '{"queue_id": %s}' % str_type_object

        # Act
        response = self.app.post('/add_to_queue/',
                           content_type='application/json',
                           data=payload)

        # Assert
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
