import json
import yaml
import mysql.connector
from mysql.connector import errorcode


### Load the config file
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config)
  
### load the json file
with open(config['data_path']) as f:
    data = json.load(f)
  
print(data)

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
        print('Now using databse ' + config['db_name'])
        login_success = True 
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist, please check the configuration in config.yaml')
            # if database name is wrong, there is no point in asking for credentials again
            break
        else:
            print(err)
            print('Please re-enter your details.')
    else:
        cnx.close()

### Write data into the sql server

### Continuously accept queries


### Allow the user to quit

