1.)
[mdo572@isp02 homework06]$ kubectl apply -f mdo572-test-redis-PVC.yml 
persistentvolumeclaim/mdo572-test-pvc created

2.)
[mdo572@isp02 homework06]$ kubectl apply -f mdo572-test-redis-deployment.yml 
deployment.apps/mdo572-test-redis-deployment created

3.)
[mdo572@isp02 homework06]$ kubectl apply -f mdo572-test-redis-service.yml 
service/mdo572-test-redis-service created

4.)
[mdo572@isp02 homework06]$ kubectl apply -f mdo572-test-flask-deployment.yml 
deployment.apps/mdo572-test-flask-deployment created

5.)
[mdo572@isp02 homework06]$ kubectl apply -f mdo572-test-flask-service.yml 
service/mdo572-test-flask-service created


