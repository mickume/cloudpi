# Infrastructure Setup

```shell

# create the address space
oc apply -f deployments/cloudpi-address-space.yaml -n cloudpi-clients

# create queues
oc apply -f deployments/cloudpi-sensor-queue.yaml -n cloudpi-clients

# create users
oc apply -f deployments/cloudpi-cloudpi1-user.yaml -n cloudpi-clients

```

```shell

oc get addressspace -o yaml -n cloudpi-clients

oc get addressspace -n cloudpi-clients -o 'jsonpath={.status.endpointStatuses[?(@.name=="messaging")].externalHost}'

#oc get addressspace -n cloudpi-clients -o yaml | grep 'externalHost: mqtt' | awk -F": " '{print $2}'
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="messaging")].externalHost}'
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="mqtt")].externalHost}'

# get the public keys
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.caCert}' | base64 -D > root.pem
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="mqtt")].cert}' | base64 -D > mqtt.pem
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="messaging")].cert}' | base64 -D > amqp.pem

oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="mqtt")].externalHost}'
```
