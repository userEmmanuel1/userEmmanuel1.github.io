import psycopg2
from flask import Flask
import multiprocessing
\
##### WORKS NOW DO NOT TOUCH AGAIN  4-18 
print("THE DATBASE.PY SCRIPT WORKS TEST 1")

user_info = None
conn = None
cur = None







#Gets the users info once from app.py and passes into database 
def create_database(tracking_stocks, email_sms_value, selected_option, name):

    try:
        conn = psycopg2.connect(host="::1", dbname="postgres", user="postgres", password="Cueva123", port=5433)
        cur = conn.cursor() 

        # 
        user_name = name
        user_email = email_sms_value
        user_membership = selected_option
        user_stock = tracking_stocks
        print("CONNECTED TO DATABASE")

       

        # Creating table if not exists
        create_table_query = '''CREATE TABLE IF NOT EXISTS Investiwatcher_users (
                                user_name VARCHAR(50),
                                user_email VARCHAR(50) PRIMARY KEY,
                                user_membership VARCHAR(20),
                                user_stock VARCHAR(20)
                            )'''
        cur.execute(create_table_query)
        
        # Inserting user information into the table
        insert_query = "INSERT INTO Investiwatcher_users (user_name, user_email, user_membership, user_stock) VALUES (%s, %s, %s, %s)"
        cur.execute(insert_query, (user_name, user_email, user_membership, user_stock))
        print("Should have entered database" )
        
        
        conn.commit()

    except Exception as error:
        print(error)

    finally: 
        if cur is not None: 
            cur.close()
        if conn is not None:
            conn.close()

print("THE DATBASE.PY SCRIPT WORKS TEST 2")

# Create an instance of user_info


# Call the create_database function with user_info
create_database('AAPL', 'VSCODE@GMAIL.TEST', 'HOURLY', 'PANYWHERE')
