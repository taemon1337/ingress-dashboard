#!/bin/sh
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <output-json-file>" >&2
  exit 1
fi

JSONFILE="$1"
SLEEP="${SLEEP:-3000}"
APISERVER="${APISERVER:-https://kubernetes.default.svc}"
SERVICEACCOUNT="${SERVICEACCOUNT:-/var/run/secrets/kubernetes.io/serviceaccount}"
ENDPOINT="${ENDPOINT:-api/networking.k8s.io/v1/ingresses}"
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)
TOKEN=$(cat ${SERVICEACCOUNT}/token)
CACERT=${SERVICEACCOUNT}/ca.crt

while true; do
  if curl --fail -v -o "${JSONFILE}" --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/${ENDPOINT} ; then
    echo "[SUCCESS] $(date) Downloaded ${ENDPOINT} to ${JSONFILE}"
  else
    echo "[FAIL] $(date) Error downloading ${ENDPOINT}"
  fi
  sleep "${SLEEP}"
done