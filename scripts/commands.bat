## deploy mysql
oc apply -f mysql-pvc.yaml
oc apply -f mysql-secret.yaml
oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml


## deploy mysql dal
oc new-app benny2025r/sql_dal:4
oc expose deployment sql-dal --name sql-dal --port 8000 --target-port 8000
oc expose service sql-dal
oc get route sql-dal



