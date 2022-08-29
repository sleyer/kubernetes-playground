# Introduction

This is a simple webserver based on python to return a simple "Hello World" as html. 

# Building the container

To build the webserver as a container, run: 

```
docker build --tag python-webserver .
```

# Running the container

To run the container, execute: 

```
 docker run --publish 8080:8080 python-webserver
```

This exposes the container to the port 8080. If you want the container to listen on a different port, change the 
first port variable accordingly. 


# Deploying it into kubernetes

## local testsetup with minikube

### Setup minikube

You need to run these commands once on your machine: 

```
# no ingresses without this:
minikube addons enable ingress 
```

### Run in minikube

Build the image for the minikube docker environment: 

```
eval $(minikube docker-env)
docker build --tag python-webserver .
```

Now, you can run it in minikube: 

```
kubectl apply -k ./Kubernetes/base
```

And when you don't need it anymore, delete it:

```
kubectl delete -k ./Kubernetes/base
```