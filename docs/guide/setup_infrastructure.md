# Overview

The next section shows how to install the MQTT messaging infrastructure, how to create a basic configuration and how to query messaging endpoints. 

### Install Enmasse

```shell
cd bin/enmasse-*

export ENMASSE=enmasse-infra
oc new-project $ENMASSE

oc apply -f install/bundles/enmasse -n $ENMASSE

oc apply -f install/components/example-plans -n $ENMASSE
oc apply -f install/components/example-roles -n $ENMASSE
```

### Authentication Service

```shell
oc apply -f install/components/example-authservices/standard-authservice.yaml -n $ENMASSE
```

### Create an address space

```shell
oc apply -f deployments/cloudpi-mqtt/cloudpi-address-space.yaml -n cloudpi-mqtt
```

### Create queues

```shell
oc apply -f deployments/cloudpi-mqtt/cloudpi-sensor-queue.yaml -n cloudpi-mqtt
```

### Create users

```shell
oc apply -f deployments/cloudpi-mqtt/cloudpi-user.yaml -n cloudpi-mqtt
```

### Query address space metadata


#### Get all metadata

```shell
oc get addressspace -o yaml -n cloudpi-mqtt
```

#### Get endpoint hostnames

```shell
oc get addressspace -n cloudpi-mqtt -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="messaging")].externalHost}'

oc get addressspace -n cloudpi-mqtt -o=jsonpath='{.items[0].status.endpointStatuses[?(@.name=="mqtt")].externalHost}'
```

### Uninstall Enmasse

```shell
oc delete clusterrolebindings -l app=enmasse
oc delete crd -l app=enmasse
oc delete clusterroles -l app=enmasse
oc delete apiservices -l app=enmasse
oc delete oauthclients -l app=enmasse

oc delete deployment -l app=enmasse
oc delete svc -l app=enmasse
```