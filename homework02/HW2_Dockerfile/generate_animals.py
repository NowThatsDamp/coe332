#!/usr/bin/env python3
import json
import random
import petname
import sys

headList = ['snake', 'bull', 'lion', 'raven','bunny']

data = {}
data['animals'] = []
for x in range(20):
	data['animals'].append( {'head' : headList[random.randint(0,4)], 
				 'body' : random.choice(petname.names) + '-' + random.choice(petname.names),
		        	 'arms' : 2 * random.randint(1,5),
				 'legs' : 3 * random.randint(1,4),
		        	 'tail' : []  } )
	data['animals'][x]['tail'] = data['animals'][x]['arms'] + data['animals'][x]['legs'] 

with open(sys.argv[1], 'w') as out:
    json.dump(data, out, indent=2)
