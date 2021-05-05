import os
from jobs import q, update_job_status
import time
POD_IP = os.environ.get('POD_IP')
if not POD_IP:
    raise Exception()

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress', POD_IP)
    time.sleep(15)
    update_job_status(jid, 'complete', POD_IP)
execute_job()
