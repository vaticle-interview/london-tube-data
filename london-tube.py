import json
  
f = open('train-network.json', 'r')
  
data = json.load(f)
  
print(data)