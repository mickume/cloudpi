#/bin/bash
source ../config

for i in `seq 1 $NUM_USERS`
do
   PROJECT_NAME="$PROJECT_BASE_NAME${i}"

   oc delete project $PROJECT_NAME
done

