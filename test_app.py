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
    INSPECTION = True

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

        # Insert X number of empty rows
        num_of_test_row = 10000
        execute_query('INSERT INTO public.migration_id VALUES (DEFAULT);', num_of_test_row)

    def tearDown(self):
        if self.INSPECTION is False:
            execute_query('TRUNCATE TABLE public.migration_id;')

    def test_add_item_to_queue(self):
        # Arrange - get all unprocessed queue ids
        queue_sql = 'SELECT queue_id FROM public.migration_id WHERE added_to_queue IS NULL;'
        queue_ids = execute_query(queue_sql)

        # Act
        for row in queue_ids:

            payload = '{"queue_id": %s}' % row[0]

            rv = self.app.post('/add_to_queue/',
                               content_type='application/json',
                               data=payload)

            # Assert response only
            self.assertEqual(rv.status_code, 200)
            self.assertEqual(rv.data, '{} added to queue'.format(row[0]).encode())

if __name__ == '__main__':
    unittest.main()
