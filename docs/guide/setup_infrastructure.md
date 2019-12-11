# Infrastructure Setup

### Create an address space

#### Without own SSL

```shell

# create the address space
oc apply -f deployments/cloudpi-mqtt/cloudpi-address-space.yaml -n cloudpi-clients

```

#### With own SSL

```shell

#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout cloudpi.key -out cloudpi.pem

openssl req -x509 -newkey rsa:2048 -keyout cloudpi_private.pem -nodes -out cloudpi.pub -subj /CN=unused

cat cloudpi_private.pem | base64 > cloudpi_private64.pem
cat cloudpi.pub | base64 > cloudpi64.pub

# make a copy of deployments/cloudpi-address-space-cert.yaml
cp deployments/cloudpi-address-space-cert.yaml deployments/cloudpi-address-space-mycert.yaml

# add the base64 encode parts 
# ...

# apply 
oc apply -f deployments/cloudpi-address-space-mycert.yaml -n cloudpi-clients

```

### Create queues and users

```shell

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
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.caCert}' | base64 -D > messaging_client/src/ca_cert.pem
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="mqtt")].cert}' | base64 -D > mqtt_cert.pem
oc get addressspace -n cloudpi-clients -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="messaging")].cert}' | base64 -D > amqp_cert.pem
mv *.pem messaging-clients/src/

```
