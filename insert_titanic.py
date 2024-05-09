import psycopg2
from queries import CREATE_TITANIC_TABLE
import csv

DNAME = 'pjksxssb'
USER = 'pjksxssb'
PASSWORD = 'wK01rRzqfi2AHOcB0wHEQRlzwCK4sj0X'
HOST = 'jelani.db.elephantsql.com'

def connect_to_pg(dbname = DNAME, user = USER, password = PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname = DNAME, user = USER, password = PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, query, data= None):
    if data:
        curs.execute(query, data)
    else:
        curs.execute(query)
    conn.commit()

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def insert_data(conn, curs, data):
    for row in data[1:]:
        if len(row) == 8:
            insert_query = '''INSERT INTO titanic_table ("Survived", "Pclass", "Name", "Sex", "Age", "Siblings/Spouses Aboard", "Parents/Children Aboard", "Fare")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

            modify_db(conn, curs, insert_query, row)
        else:
             print("Skipping row as it doesn't have the correct number of columns:", row)


if __name__ == "__main__":
    # Get data from csv File
    csv_data = read_csv("C:/Users/ISHMO_CT/Downloads/Bloomtech/sv-to-post/titanic.csv")

    # Create the desitantion file in postgress
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, CREATE_TITANIC_TABLE)

    # Insert data in to postgress. 
    insert_data(pg_conn, pg_curs, csv_data)

    # close connection 
    pg_curs.close()
    pg_conn.close()

    




