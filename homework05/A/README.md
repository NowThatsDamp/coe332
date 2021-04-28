1.)
	-yml file is found in this folder. It is called "pod-basic.yml"
	-Command used:
		- apply -f pod-basic.yml
2.)
	- Command used:
		- kubectl get pods --selector "greeting=personalized"
	- Output:
		- NAME    READY   STATUS    RESTARTS   AGE
		  hello   1/1     Running   0          9m50s
3.)
	- logs output:
		- Hello,
	- This is what I would expect given that the environment variable NAME
	  does not yet have a value
4.)
	- Command used:
		- kubectl delete pods hello
