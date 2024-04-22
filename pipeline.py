import psycopg2

DNAME = 'pjksxssb'
USER = 'pjksxssb'
PASSWORD = 'wK01rRzqfi2AHOcB0wHEQRlzwCK4sj0X'
HOST = 'jelani.db.elephantsql.com'

def connect_to_pg(dbname = DNAME, user = USER, password = PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname = DNAME, user = USER, password = PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()


if __name__ == "__main__":
    # Get data from csv File


    # Create the desitantion file in postgress
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, CREATE_TITANIC_TABLE)
    




