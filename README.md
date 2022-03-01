# Ingress Dashboard
A simple UI to use as a default Ingress into your Kubernetes cluster.

## Why?
If you have ever tried to visit an Ingress host on a Kubernetes cluster and been confronted with a 404 or some other error, this project will provide a simple landing page that will list all the available Ingresses at their registered locations.

## How?
Most ingress controllers allow a default service to be used when no route matches an incoming request, this project will serve a simpe UI listing all the Ingresses so that users can find the correct location.

## Screenshot
![Screenshot](/docs/screenshot.png?raw=true "Ingress Dashboard Screenshot")