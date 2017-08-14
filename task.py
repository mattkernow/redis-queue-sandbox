import psycopg2


DB_CONNECTION = "dbname=queue host=localhost port=5432 user=postgres password=postgres"


def insert_into_db(queue_id, add_to_queue_date):
    # Task to be run asynchronously by Redis worker

    # Connect the db for each queue item to slow the completion of each task
    conn = psycopg2.connect(DB_CONNECTION)

    # Insert the record into the postgres table
    cur = conn.cursor()
    query_str = 'INSERT INTO public.migration_id (queue_id, added_to_queue, written_to_table) VALUES (%s, %s, DEFAULT);'
    cur.execute(query_str, (queue_id, add_to_queue_date))

    conn.commit()
    cur.close()
    conn.close()
