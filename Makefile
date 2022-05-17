SHELL=/bin/bash

chart:
	helm package deploy/helm/ingress-dashboard
