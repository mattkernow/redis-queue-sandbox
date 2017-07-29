import psycopg2

def insert_into_db(job_id):
    # Connect to an existing database
    conn = psycopg2.connect("dbname=queue user=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute("select * from public.migration_id")

