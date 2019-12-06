# Infrastructure

### Install EnMasse

```shell

cd bin/enmasse-*

export ENMASSE=enmasse-infra
oc new-project $ENMASSE

oc apply -f install/bundles/enmasse -n $ENMASSE

oc apply -f install/components/example-plans -n $ENMASSE
oc apply -f install/components/example-roles -n $ENMASSE
oc apply -f install/components/example-authservices/standard-authservice.yaml -n $ENMASSE

```

### Remove EnMasse

```shell

oc delete clusterrolebindings -l app=enmasse
oc delete crd -l app=enmasse
oc delete clusterroles -l app=enmasse
oc delete apiservices -l app=enmasse
oc delete oauthclients -l app=enmasse

```
