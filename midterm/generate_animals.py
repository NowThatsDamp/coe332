import json
import random
import petname
import uuid
import redis
import datetime

rd = redis.StrictRedis(host='127.0.0.1', port = 6404, db=0)
rd.flushall
headList = ['snake', 'bull', 'lion', 'raven','bunny']

data = {}
data['animals'] = []
for x in range(20):
	data['animals'].append( {'created_on' : str('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())),
							 'uid' : str(uuid.uuid4()),
							 'head' : headList[random.randint(0,4)], 
				 			 'body' : random.choice(petname.names) + '-' + random.choice(petname.names),
		        		 	 'arms' : random.randint(2,10),
				 			 'legs' : random.randint(3,12),
		        			 'tail' : []  } )
	data['animals'][x]['tail'] = data['animals'][x]['arms'] + data['animals'][x]['legs'] 

rd.set('k1', json.dumps(data))
print(json.loads(rd.get('k1')))
