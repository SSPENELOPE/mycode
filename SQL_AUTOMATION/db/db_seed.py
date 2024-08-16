import mysql.connector
from mysql.connector import Error
import random
from faker import Faker

# Configuration for MySQL connection
mysql_config = {
    'host': '192.168.1.72',
    'port': 3306,
    'user': 'root',
    'password': '123456789',
    'database': 'starcontractor_db'
}

# List of allowed starting areas
starting_areas = [
    'Lorville',
    'Grim Hex',
    'New Babbage',
    'Area 18'
]

# Create a Faker instance
fake = Faker()

def generate_users(num_users):
    users = []
    for _ in range(num_users):
        user = {
            'email': fake.email(),
            'starting_area': random.choice(starting_areas),
            'username': fake.user_name(),
            'password': fake.password(),
            'admin': random.choice([True, False]),
            'verified': random.choice([True, False])
        }
        users.append(user)
    return users

def seed_users(users):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**mysql_config)
        if conn.is_connected():
            cursor = conn.cursor()

            # SQL query to insert user data, we can update this as needed
            insert_query = """
            INSERT INTO user (email, starting_area, username, password, admin, verified)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            # Execute the insert query for each user
            cursor.executemany(insert_query, [
                (user['email'], user['starting_area'], user['username'], user['password'], user["admin"], user["verified"])
                for user in users
            ])
            conn.commit()

            print(f"Inserted {len(users)} users into the database.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    num_users_to_insert = 1000  # Adjust the number of users as needed
    users = generate_users(num_users_to_insert)
    seed_users(users)