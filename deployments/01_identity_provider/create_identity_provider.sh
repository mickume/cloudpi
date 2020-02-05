#/bin/bash
source ../config

SUPERUSER='user0'

if [ -f $TEMP_PWD_FILE ]; then
   rm $TEMP_PWD_FILE
fi

# create the htpassword file
htpasswd -c -B -b $TEMP_PWD_FILE $SUPERUSER_NAME $SUPERUSER_DEFAULT_PWD
for i in `seq 1 $NUM_USERS`
do
   htpasswd -b $TEMP_PWD_FILE $USER_BASE_NAME${i} $USER_DEFAULT_PWD
done

# create the secret
oc delete secret htpass-secret -n openshift-config
oc create secret generic htpass-secret --from-file=htpasswd=$TEMP_PWD_FILE -n openshift-config

# deploy the custom identity provider (htpass based)
oc apply -f identity_provider_cr.yaml

# create a superuser
oc create user $SUPERUSER_NAME
oc adm policy add-cluster-role-to-user cluster-admin $SUPERUSER_NAME

# create the rest of the users
for i in `seq 1 $NUM_USERS`
do
   USER_NAME="$USER_BASE_NAME${i}"
   oc create user $USER_NAME
done

# cleanup
rm $TEMP_PWD_FILE