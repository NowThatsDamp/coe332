import os
from jobs import q, rd, update_job_status, rdata
import time
from matplotlib import pyplot as plt
POD_IP = os.environ.get('POD_IP')
if not POD_IP:
    raise Exception()
@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress', POD_IP)
    data = rdata.hgetall('data')
    x = []
    y = []
    for key in sorted(data.keys()):
        x.append(key)
        y.append(float(data[key]))
    plt.plot(x, y)
    plt.title('Year Average Fuel Cost at Austin Energy')
    plt.xlabel('Year')
    plt.ylabel('Cents per KW/h')
    plt.savefig(f'/tmp/{jid}_output_image.png') 
    with open(f'/tmp/{jid}_output_image.png', 'rb') as f:
        img = f.read()
    rd.hset(jid, 'image', img)
    rd.hset(jid, 'status', 'complete')
execute_job()
