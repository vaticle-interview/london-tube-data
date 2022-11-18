import json
import yaml
import mysql.connector
from mysql.connector import errorcode


### Load the config file
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# print(config)
  
### load the json file
with open(config['data_path']) as f:
    data = json.load(f)
  
# print(data)

### Write data into the sql server
## Establish a connection with the sql server

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

# Update the database schema accordign to the sql file
with open(config['schema_path']) as f:
    file_content = f.read()
    
commands = file_content.split(';')

for command in commands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        cursor.execute(command)
    except mysql.connector.Error as err:
        print(err)

# try:
#     print("Updating database schema")
#     for result in cursor.execute(f, multi=True):
#         if result.with_rows:
#             print("Rows produced by statement '{}':".format(result.statement))
#             print(result.fetchall())
#         else:
#             print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))

#     print("Successfully updated database schema specified in {}".format(config['schema_path']))
# except mysql.connector.Error as err:
#     print(err)


cursor.close()
cnx.close()

### Continuously accept queries

## Use "list stations" or "list lines" to see all the stations/lines


### Allow the user to quit

