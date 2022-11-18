import json
import yaml
# TODO refactor the code using logger
import logging
import mysql.connector
from mysql.connector import errorcode

# Colours for prettier printing
# Copied from joeld and Peter Mortensen
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

#TODO extract a function "execute command"

# Update the database schema accordign to the sql file
with open(config['schema_path']) as f:
    file_content = f.read()
commands = file_content.split(';')

for command in commands:
    # For prettier printing
    command = command.strip()
    try:
        print('Executing the following sql command')
        print('------------------------------------------------')
        print(command)
        print('------------------------------------------------')
        cursor.execute(command)
        print(f'{bcolors.OKGREEN}Success{bcolors.ENDC}')
    except mysql.connector.Error as err:
        print(f'{bcolors.FAIL}err{bcolors.ENDC}')
print('Updated database schema specified in {}'.format(config['schema_path']))

## Insert data
stations_data = data['stations']
for row in stations_data:
    id = row['id']
    name = row['name']
    print(id)
    print(name)



cnx.commit()
### Continuously accept queries

## TODO Use "list stations" or "list lines" to see all the stations/lines


cursor.close()
cnx.close()

### TODO Allow the user to quit

