import mysql.connector

try:
    # Establish connection to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password1234"
    )

    # Create a cursor object to execute SQL queries
    my_cursor = mydb.cursor()

    # Create a new database named 'our_users'
    #my_cursor.execute("CREATE DATABASE IF NOT EXISTS our_users")

    # Execute a query to show all databases
    my_cursor.execute("SHOW DATABASES")

    # Fetch and print the list of databases
    for db in my_cursor:
        print(db)

    # Close cursor and database connection
    my_cursor.close()
    my_db.close()

except mysql.connector.Error as err:
    print("Error:", err)
