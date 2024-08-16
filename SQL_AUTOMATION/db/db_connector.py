import pandas as pd
from sqlalchemy import create_engine
import yaml

def process_boolean_values(df):
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].apply(lambda x: "False" if x == b'\x00' else "True" if x == b'\x01' else x)
    return df

def fetch_data():
    # Read the configuration from db_config.yaml
    with open('db_config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Extract MySQL configuration
    mysql_config = config['mysql']
    
    # Construct the database URL
    db_url = f"mysql+pymysql://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}"

    # Create an SQLAlchemy engine
    engine = create_engine(db_url)

    # Prompt the user to choose a table
    table_name = input("Enter the table name you want to query: ")

    # Execute a query to fetch all rows from the selected table
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)

    # Dispose of the engine
    engine.dispose()
    
    process_boolean_values(df)

    return df