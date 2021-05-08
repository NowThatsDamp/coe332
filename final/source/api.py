import json
import uuid
import hotqueue
import jobs
import os
import redis
from flask import Flask, request, send_file

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()

app = Flask(__name__)
rd = redis.StrictRedis(host=redis_ip, port=6379, db=0)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!\n'

@app.route('/clear_jobs', methods=['GET'])
def clear_jobs():
    for key in rd.keys():
        rd.delete(key)
        print(key)
    return 'Deleted\n'

@app.route('/download_data', methods=['GET'])
def download_data():
    jobs.download()
    return 'Printed.\n'

@app.route('/download/<jobid>', methods=['GET'])
def download(jobid):
    path = f'/tmp/{jobid}_output_image.png'
    with open(path, 'wb') as f:
        f.write(rd.hget(jobid, 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json(force=True)
    year = int(json.dumps(data['year']))
    cost = float(json.dumps(data['cost']))
    jobs.rdata.hset('data', year, cost)
    return'Data updated.\n'

@app.route('/run', methods=['POST'])
def run_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
