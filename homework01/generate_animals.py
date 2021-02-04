import json
import random
import petname

headList = ['snake', 'bull', 'lion', 'raven','bunny']

data = {}
data['animals'] = []
for x in range(20):
	data['animals'].append( {'head' : headList[random.randint(0,4)], 
				 'body' : random.choice(petname.names) + '-' + random.choice(petname.names),
		        	 'arms' : random.randint(2,10),
				 'legs' : random.randint(3,12),
		        	 'tail' : []  } )
	data['animals'][x]['tail'] = data['animals'][x]['arms'] + data['animals'][x]['legs'] 

with open('animals.json', 'w') as out:
    json.dump(data, out, indent=2)
