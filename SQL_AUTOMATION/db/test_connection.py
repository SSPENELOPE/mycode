import mysql.connector
import yaml

# Load configuration
with open('db_config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Extract MySQL configuration
mysql_config = config['mysql']

try:
    # Attempt to connect to MySQL
    conn = mysql.connector.connect(**mysql_config)
    print("Connection successful!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")