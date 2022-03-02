# Ingress Dashboard
A simple UI to use as a default Ingress into your Kubernetes cluster.

## Why?
If you have ever tried to visit an Ingress host on a Kubernetes cluster and been confronted with a 404 or some other error, this project will provide a simple landing page that will list all the available Ingresses at their registered locations.

## How?
Most ingress controllers allow a default service to be used when no route matches an incoming request, this project will serve a simpe UI listing all the Ingresses so that users can find the correct location.

## Screenshot
![Screenshot](/docs/screenshot.png?raw=true "Ingress Dashboard Screenshot")

## Getting Started
A Helm chart is provided at [deploy/helm][./deploy/helm/ingress-dashboard] and can be installed as follows:

```
  git clone git@github.com:taemon1337/ingress-dashboard.git
  helm install ./ingress-dashboard/deploy/helm/ingress-dashboard
```

See your Ingress Controller documentation for how to set a default backend; for `nginx-ingress` there is a `--default-backend-service` [cli argument](https://kubernetes.github.io/ingress-nginx/user-guide/cli-arguments/) that can be set to `ingress-dashboard/ingress-dashboard` if you don't modify the release name.

## Ingress Annotations
The Dashboard will use the `ingress.metadata.name` to attempt to load an accurate project photo for the ingress if the ingress is named after the project, i.e. `longhorn-ingress` will load the "longhorn" icon.  You can use the following `annotations` on the Ingress resource to tell the Dashboard you want to use specific values in the Dashboard.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <project-name>-ingress
  annotations:
    "dashboard-title": "My Falco Service"
    "dashboard-image": "/img/falco"
    "dashboard-host": "myservice.mycluster.com"
    "dashboard-href": "myservice.mycluster.com/falco/ui"
```

