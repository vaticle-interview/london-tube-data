import json
import yaml
import mysql.connector
from tables import TABLES
from mysql.connector import errorcode


### Load the config file
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# print(config)
  
### load the json file
with open(config['data_path']) as f:
    data = json.load(f)
  
# print(data)

### Establish a connection with the sql server

# Create the connection with error handling
login_success = False

# If wrong credentials were entered, ask again.
while not login_success:
    # Prompt the user to enter credentials
    username = input('Username: ')
    password = input('Password: ')
    try:
        cnx = mysql.connector.connect(user=username,
                                        password=password,
                                        database=config['db_name'])
        print('Successfully established connection with MySQL server')
        login_success = True 
    except mysql.connector.Error as err:
        print(err)
        print('Please re-enter your details.')

cursor = cnx.cursor()
## Write data into the sql server

# Use the correct databse
# Create one if it does not exist

db_name = config['db_name']

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(db_name))
        cnx.database = db_name
    else:
        print(err)
        exit(1)
print('Now using database {}'.format(db_name))

# Create tables 
# TODO drop the old table if already exists
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

### Continuously accept queries

## Use "list stations" or "list lines" to see all the stations/lines


### Allow the user to quit

