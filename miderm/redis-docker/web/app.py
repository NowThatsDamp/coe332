import json
import redis
from flask import Flask

rd = redis.StrictRedis(host='redis', port = 6379, db=0)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, worlds!\n'

@app.route('/animals/head/<head>', methods=['GET'])
def get_head(head):
    return json.dumps(read_head(head))

@app.route('/animals', methods=['get'])
def get_animals():
	return get_data()

@app.route('/animals/legs/<num>', methods=['get'])
def get_legs(num):
	return json.dumps(read_legs(num))

def read_legs(num):
	with open("animals.json", "r") as json_file:
		animal_list = json.load(json_file)
	data = {}
	data['animals'] = []
	for i in animal_list['animals']:
		if(str(i['legs']) == num):
			print(i)
			data['animals'].append(i)
	return data

def read_head(head_shape):
	with open("animals.json", "r") as json_file:
		animal_list = json.load(json_file)

	data = {}
	data['animals'] = []
	for i in animal_list['animals']:
		if(i['head'] == head_shape):
			data['animals'].append(i)
	return data

def get_data():	   
	with open("animals.json", "r") as json_file:
		userdata = json.load(json_file)
	return userdata

if  __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')
