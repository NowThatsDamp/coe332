1.)
	- The yml file is included in this folder. It is named "deployment.yml"
	- Command used:
	 	- kubectl apply -f deployment.yml
2.) 
	- Command and output:
		- [mdo572@isp02 C]$ kubectl get pods -o wide
		  NAME                            READY   STATUS    RESTARTS   AGE     IP              NODE   NOMINATED NODE   READINESS GATES
		  hello-deploy-59b6866c56-6w5fw   1/1     Running   0          5m43s   10.244.12.243   c12    <none>           <none>
		  hello-deploy-59b6866c56-7b8q8   1/1     Running   0          5m43s   10.244.7.216    c05    <none>           <none>
		  hello-deploy-59b6866c56-gtfff   1/1     Running   0          5m43s   10.244.15.10    c03    <none>           <none>
3.)
	- The logs match the results in 2. Each pod declared not only the NAME variable it was assigned, but also its own IP address
	  as listed in problem 2
	- Command and output:
		- [mdo572@isp02 C]$ kubectl logs hello-deploy-59b6866c56-6w5fw
		  Hello, Michael from 10.244.12.243

		  [mdo572@isp02 C]$ kubectl logs hello-deploy-59b6866c56-7b8q8
		  Hello, Michael from 10.244.7.216

		  [mdo572@isp02 C]$ kubectl logs hello-deploy-59b6866c56-gtfff
		  Hello, Michael from 10.244.15.10
