import json
import mysql.connector
from mysql.connector import errorcode
  
### load the json file
f = open('train-network.json', 'r')
  
data = json.load(f)
  
print(data)

### Establish a connection with the sql server

# Prompt the user to enter credentials
username = input('Username: ')
password = input('Password: ')


try:
  cnx = mysql.connector.connect(user=username,
                                password=password,
                                database='london-tube')
  print('Successfully established connection with MySQL server')
except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
    print(err)
else:
  cnx.close()

### Write data into the sql server

### Continuously accept queries


### Allow the user to quit

