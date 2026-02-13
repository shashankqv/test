import mysql.connector

# Replace with your own database connection details

config = {
    'user': 'your_username',    
    'password': 'your_password',  
    'host': '127.0.0.1',  
    'database': 'your_database'
}

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('Connected to MySQL database')
except mysql.connector.Error as err:
    print(f'Error: {err}')
finally:
    if connection.is_connected():
        connection.close()
        print('Connection closed')
