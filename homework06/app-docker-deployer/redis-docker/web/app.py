import json
import random
import petname
import uuid
import datetime
import redis
import flask
import os
from flask import Flask, request

app = Flask(__name__)

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=redis.StrictRedis(host=redis_ip, port=6379, db=0)

@app.route('/reset', methods=['GET'])
def reset():
    generate_animals()
    return 'Animals reset\n'    

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!\n'

@app.route('/dates', methods=['GET'])
def get_dates():
    check()
    start = request.args.get('start')
    startdate = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = request.args.get('end')
    enddate = datetime.datetime.strptime(end, '%Y-%m-%d')
    data = json.loads(rd.get('k1'))['animals']
    return_data = {}
    return_data['animals'] = []
    for x in data:
        if (datetime.datetime.strptime(x['created_on'], '%Y-%m-%d') >= startdate and datetime.datetime.strptime(x['created_on'], '%Y-%m-%d')<= enddate):
            return_data['animals'].append(x)
    return json.dumps(return_data)

@app.route('/length', methods=['GET'])
def length():
    check()
    data = json.loads(rd.get('k1'))['animals']
    return str(len(data))

@app.route('/average', methods=['GET'])
def average():
    check()
    data = json.loads(rd.get('k1'))['animals']
    i = 0
    q = 0
    for x in data:
        q = q+1
        i = i+x['legs']
    average = i/q 
    return str(average)

@app.route('/deletedates', methods=['GET'])
def delete_dates():
    check()
    start = request.args.get('start')
    startdate = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = request.args.get('end')
    enddate = datetime.datetime.strptime(end, '%Y-%m-%d')
    data = json.loads(rd.get('k1'))['animals']
    return_data = {}
    return_data['animals'] = []
    for x in data:
        if (datetime.datetime.strptime(x['created_on'], '%Y-%m-%d') < startdate and datetime.datetime.strptime(x['created_on'], '%Y-%m-%d') > enddate):
            return_data['animals'].append(x)
        else:
            print('delete hit')
    for key in rd.keys():
        print('key updated')
        rd.delete(key)
    rd.set('k1', json.dumps(return_data))
    print(json.loads(rd.get('k1')))
    return 'Keys deleted\n'

@app.route('/uuid', methods=['GET'])
def get_uuid():
    check()
    uuid = request.args.get('uuid')
    return_data = return_by_uuid(uuid)
    return json.dumps(return_data)

@app.route('/update', methods=['GET'])
def update():
    uuid = request.args.get('uuid')
    head = request.args.get('head')
    body = request.args.get('body')
    arms = request.args.get('arms')
    legs = request.args.get('legs')
    tail = request.args.get('tail')
    data = json.loads(rd.get('k1'))['animals']
    for x in data:
        if(x['uid'] == uuid):
            if(head != None):
                x['head'] = head
            if(body != None):
                x['body'] = body
            if(arms != None):
                x['arms'] = arms
            if(legs != None):
                x['legs'] = legs
            if(tail != None):
                x['tail'] = tail
            return_data = {}
            return_data['animals'] = data
            for key in rd.keys():
                print('key updated')
                rd.delete(key)
            rd.set('k1', json.dumps(return_data))
            return x
    return 'UUID not found\n'

def return_by_uuid(uid):
    uuid = request.args.get('uuid')
    data = json.loads(rd.get('k1'))['animals']
    return_data = {}
    return_data['animals'] = []
    for x in data:
        if(x['uid'] == uuid):
            return_data['animals'].append(x)
    return return_data


def generate_animals():
    print("Generate hit")
    headList = ['snake', 'bull', 'lion', 'raven','bunny']
    for key in rd.keys():
        print('key deleted')
        rd.delete(key)
    data = {}
    data['animals'] = []
    for x in range(20):
        print("Loop hit")
        data['animals'].append( {'created_on' : '{:%Y-%m-%d}'.format(datetime.datetime.now()),
                                 'uid' : str(uuid.uuid4()),
                                 'head' : headList[random.randint(0,4)],
                                 'body' : random.choice(petname.names) + '-' + random.choice(petname.names),
                                 'arms' : (random.randint(1,5)*2),
                                 'legs' : (random.randint(1,4)*3),
                                 'tail' : []  } )
        data['animals'][x]['tail'] = data['animals'][x]['arms'] + data['animals'][x]['legs']
    rd.set('k1', json.dumps(data))
    return

def check():
    if rd.keys() == []:
        generate_animals()
    print('List Checked')
    return

if  __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
