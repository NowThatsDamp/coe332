import uuid
import os
import json
from hotqueue import HotQueue
from redis import StrictRedis
import pandas

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=StrictRedis(host=redis_ip, port=6379, db=0)
rdata=StrictRedis(host=redis_ip, port=6379, db=2, decode_responses=True)
q = HotQueue("queue", host=redis_ip, port=6379, db=1)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }

def _instantiate_job_IP(jid, status, start, end, POD_IP):
    if type(jid) == str:
        return {'id': jid,
                'worker-ip': POD_IP,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'worker-ip': POD_IP,
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }


def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def download():
    df = pandas.read_csv('https://data.austintexas.gov/api/views/6yrz-de8g/rows.csv?accessType=DOWNLOAD', index_col='Fiscal Year', )
    dfd = df.to_dict()['System annual average fuel cost (cents/kWh)']
    new_dict = {}
    for (key,value) in dfd.items():
        new_dict[int(key.split(' ')[1])] = float(value.split(' ')[0])
    rdata.hmset('data', new_dict) 



def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status, POD_IP):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job_IP(jid, status, start, end, POD_IP)
    if job:
        job['status'] = new_status
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
