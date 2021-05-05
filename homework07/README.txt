A:
  2.)
     - [mdo572@isp02 api]$ kubectl apply -f mdo572-hw7-flask-deployment.yml 
       deployment.apps/mdo572-hw7-flask created
     - [mdo572@isp02 worker]$ kubectl apply -f mdo572-hw7-worker-deployment.yml 
       deployment.apps/mdo572-hw7-worker created
  3.)
     a:
       - [mdo572@isp02 homework07]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-t7wbt -- /bin/bash
		 root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.128:5000/jobs
		 {"id": "01b66639-25b4-41c8-9edb-a31ca75e943e", "status": "submitted", "start": "2001", "end": "2021"}
 	 b:
	   - root@py-debug-deployment-5cc8cdd65f-t7wbt:/# python3
		 Python 3.9.2 (default, Feb 19 2021, 17:11:58) 
		 [GCC 8.3.0] on linux
		 Type "help", "copyright", "credits" or "license" for more information.
		 >>> import redis
		 >>> rd=redis.StrictRedis(host='10.109.72.116', port=6379, db=0)
		 >>> for key in rd.keys():
		 ...     rd.hgetall(key)
		 ... 
		 {b'id': b'01b66639-25b4-41c8-9edb-a31ca75e943e', b'status': b'complete', b'start': b'2001', b'end': b'2021'}
		 >>> 
C:  
  a:
    - root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
      {"id": "b009b334-5445-454c-b9a9-8a080536c797", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "2a57ecdf-b365-4dd9-b96a-54c96a95759d", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "a77ac58d-0ad5-4909-9d72-1a34e8182697", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "d22896b5-4b38-46c3-b4b6-ba9c66d27931", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "a0a1f45e-9344-4a60-bad2-0834ea26a01d", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "784175bc-3e4e-42ec-8a6d-63bd8b8a8d2b", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "8421b6e9-22ec-48bf-a688-08d50c28cc78", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "9c98709b-fd1b-4078-ab95-d3e205ffec39", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "bd9e7944-f56a-47c3-a052-4008786ed629", "status": "submitted", "start": "2001", "end": "2021"}
	  root@py-debug-deployment-5cc8cdd65f-t7wbt:/# curl -X POST -H "content-type: application/json" -d '{"start": "2001", "end": "2021"}' 10.244.13.152:5000/jobs
	  {"id": "5c2797dc-1c34-45bf-8592-921f219594bb", "status": "submitted", "start": "2001", "end": "2021"}
  b: 
	- root@py-debug-deployment-5cc8cdd65f-t7wbt:/# python3
	  Python 3.9.2 (default, Feb 19 2021, 17:11:58) 
	  [GCC 8.3.0] on linux
	  Type "help", "copyright", "credits" or "license" for more information.
	  >>> import redis
	  >>> rd=redis.StrictRedis(host='10.109.72.116', port=6379, db=0)
	  >>> for key in rd.keys():
	  ...     rd.hgetall(key)
	  ... 
	  {b'id': b'd22896b5-4b38-46c3-b4b6-ba9c66d27931', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.10.93'}
	  {b'id': b'2a57ecdf-b365-4dd9-b96a-54c96a95759d', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.10.93'}
	  {b'id': b'784175bc-3e4e-42ec-8a6d-63bd8b8a8d2b', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.10.93'}
	  {b'id': b'a77ac58d-0ad5-4909-9d72-1a34e8182697', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.3.131'}
	  {b'id': b'a0a1f45e-9344-4a60-bad2-0834ea26a01d', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.3.131'}
	  {b'id': b'5c2797dc-1c34-45bf-8592-921f219594bb', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.10.93'}
	  {b'id': b'9c98709b-fd1b-4078-ab95-d3e205ffec39', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.10.93'}
	  {b'id': b'b009b334-5445-454c-b9a9-8a080536c797', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.3.131'}
	  {b'id': b'8421b6e9-22ec-48bf-a688-08d50c28cc78', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.3.131'}
	  {b'id': b'bd9e7944-f56a-47c3-a052-4008786ed629', b'status': b'complete', b'start': b'2001', b'end': b'2021', b'worker-ip': b'10.244.3.131'}
	  >>> 
  c:
    - 5 jobs were worked by each worker
