import json
import yaml
import mysql.connector
from mysql.connector import errorcode


### Load the config file
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config)
  
### load the json file
with open(config['DATA_PATH']) as f:
    data = json.load(f)
  
print(data)

### Establish a connection with the sql server

# Prompt the user to enter credentials
username = input('Username: ')
password = input('Password: ')


# Create the connection with error handling
try:
  cnx = mysql.connector.connect(user=username,
                                password=password,
                                database=config['db_name'])
  print('Successfully established connection with MySQL server')
  print('Now using databse ' + config['db_name'])
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist, please check the configuration in config.yaml")
  else:
    print(err)
else:
  cnx.close()

### Write data into the sql server

### Continuously accept queries


### Allow the user to quit

