#/bin/bash
source ../config

for i in `seq 1 $NUM_USERS`
do
   PROJECT_NAME="$PROJECT_BASE_NAME${i}"
   USER_NAME="$USER_BASE_NAME${i}"

   # create the project
   oc new-project $PROJECT_NAME

   # make the user admin for the project
   oc policy add-role-to-user admin $USER_NAME -n $PROJECT_NAME
   oc policy add-role-to-user view -n $PROJECT_NAME -z default

   # set the default resource limits
   oc delete limitrange $PROJECT_NAME-core-resource-limits -n $PROJECT_NAME
   oc create -f resource-limits.yaml -n $PROJECT_NAME
done
