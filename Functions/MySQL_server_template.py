# my sql functions for use
import mysql.connector
db_name = 'users'
query_create_new_table_with_items = """CREATE TABLE {} (
                            full_name VARCHAR(255),
                            email VARCHAR(255),
                            phone_number VARCHAR(255),
                            id VARCHAR(255),
                            notes VARCHAR(255)
                        )""".format(db_name)

query_select_from = "SELECT * FROM users"

db = mysql.connector.connect(
    host='localhost',  # ip
    user='root',
    passwd='NV27vnmc',
    database='alex_db'  # name of the db
)

class alex_sql_modules(object):
    def __init__(self, db, query_create_new_table_with_items, query_select_from):
        self.db = db
        self.query_create_new_table_with_items = query_create_new_table_with_items
        self.query_select_from = query_select_from

    def mysql_check_db_connection(self):
        print(self.db)

    def mysql_create_new_table_with_items(self):
        mycursor = self.db.cursor()
        mycursor.execute(self.query_create_new_table_with_items)
        db.commit()
        print('new table and items created')

    def mysql_print_table_and_items(self):
        # create cursor object
        mycursor = self.db.cursor()
        # execute the query define SQL query to select all items from a table
        mycursor.execute(self.query_select_from)
        # fetch all the results
        results = mycursor.fetchall()
        print(results)
        print(results[0])
        # print the results
        for row in results:
            print(row)

    def mysql_insert_items(self):
        mycursor = self.db.cursor()
        sql = "INSERT INTO users (full_name, email, phone_number, id, notes) VALUES (%s, %s, %s, %s, %s)"
        val = ("alex dezho", "alex27dz@gmail.com", "4372392986", '123456789', 'new profile')
        mycursor.execute(sql, val)
        self.db.commit()



    def mysql_delete_table(self):
        # create cursor object
        mycursor = self.db.cursor()
        # define SQL query to delete a table
        delete_query = "DROP TABLE users"
        # execute the query
        mycursor.execute(delete_query)
        print('table deleted')




    def mysql_close(self):
        self.db.close()


sql = alex_sql_modules(db, query_create_new_table_with_items, query_select_from)
sql.mysql_print_table_and_items()

