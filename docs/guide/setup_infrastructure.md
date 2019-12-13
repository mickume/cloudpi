# Overview

The next section shows how to install the MQTT messaging infrastructure, how to create a basic configuration and how to query messaging endpoints. 

### Install Enmasse

```shell
cd bin/enmasse-*

oc new-project enmasse-infra

oc apply -f install/bundles/enmasse -n enmasse-infra
```

### Install plans and infrastructure configuration

```shell
oc apply -f install/components/example-plans -n enmasse-infra
oc apply -f install/components/example-roles -n enmasse-infra
```

### Authentication Service

```shell
oc apply -f install/components/example-authservices/standard-authservice.yaml -n enmasse-infra
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