import json
import mysql.connector
  
### load the json file
f = open('train-network.json', 'r')
  
data = json.load(f)
  
print(data)

### Establish a connection with the sql server

username = input('Username: ')
password = input('Password: ')

cnx = mysql.connector.connect(user=username, password=password,
                              host='127.0.0.1',
                              database='london_tube',
                              user_pure=True)

cnx.close()

### Write data into the sql server

### Continuously accept queries


### Allow the user to quit

