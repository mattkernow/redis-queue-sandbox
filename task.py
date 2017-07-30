import psycopg2


def insert_into_db(queue_id, add_to_queue_date):
    # Connect to an existing database
    conn = psycopg2.connect("dbname=queue host=localhost port=5432 user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    query_str = """
    UPDATE public.migration_id
    SET added_to_queue=%s, written_to_table=now()
    WHERE
    queue_id=%s;
    """
    cur.execute(query_str, (add_to_queue_date, queue_id))

    conn.commit()
    cur.close()
    conn.close()
