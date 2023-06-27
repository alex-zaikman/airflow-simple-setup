# AirFlow small project

**Make sure to replace the <aws-project-id> for this project to work properly** 

## HOWTO:
```shell
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport 172.31.2.16:/ efs
```

```bash
ecs-cli compose --file docker-compose-LocalExecutor.yml --cluster flower down
```

```bash
docker build -t airflow .
```

```bash
docker tag airflow:latest <aws-project-id>.dkr.ecr.us-east-2.amazonaws.com/airflow:latest
```

```bash
docker push <aws-project-id>.dkr.ecr.us-east-2.amazonaws.com/airflow:latest
```

```bash
ecs-cli compose --file docker-compose-LocalExecutor.yml --cluster flower up
```
