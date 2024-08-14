import mysql.connector
import yaml

def fetch_data():
    # Read the configuration from config.yaml
    # with open('db_config.yaml', 'r') as config_file:
    #     config = yaml.safe_load(config_file)
    
    # mysql_config = config['mysql']

    # # Establish the connection to MySQL
    # conn = mysql.connector.connect(**mysql_config)
    
    with open('db_config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Extract MySQL configuration
    mysql_config = config['mysql']
    
    conn = mysql.connector.connect(**mysql_config)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT username, starting_area, verified FROM user")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return rows