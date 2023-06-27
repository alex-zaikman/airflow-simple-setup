# AirFlow small project
* Makesure to replace the <aws-project-id> for this project to work properly 

```shell
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport 172.31.2.16:/ efs
ecs-cli compose --file docker-compose-LocalExecutor.yml --cluster flower down
docker build -t airflow .
docker tag airflow:latest <aws-project-id>.dkr.ecr.us-east-2.amazonaws.com/airflow:latest
docker push <aws-project-id>.dkr.ecr.us-east-2.amazonaws.com/airflow:latest
ecs-cli compose --file docker-compose-LocalExecutor.yml --cluster flower up
```
