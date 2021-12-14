## Requirements
- Kubernetes 1.3+


## General informations

### Environment variables and volumes

The image recognizes the following environment variables that you can set during
initialization by passing `-e VAR=VALUE` to the Docker run command.

|  Variable name         | Description                               |
| :--------------------- | ----------------------------------------- |
|  `MYSQL_USER`          | User name for MySQL account to be created |
|  `MYSQL_PASSWORD`      | Password for the user account             |
|  `MYSQL_DATABASE`      | Database name                             |
|  `MYSQL_ROOT_PASSWORD` | Password for the root user (optional)     |

You can also set the following mount points by passing the `-v /host:/container`
flag to Docker.

| Volume mount point       | Description          |
| :----------------------- | -------------------- |
|  `/var/lib/mysql`        | MySQL data directory |

**Notice: When mouting a directory from the host into the container,
ensure that the mounted directory has the appropriate permissions and
that the owner and group of the directory matches the user UID or name
which is running inside the container.**


## Usage in Kubernetes

This image runs on kubernetes as well.

### Create cluster
```bash
$ kubectl create -f galera-volume.yaml
$ kubectl create -f galera-volume-claim.yaml
$ kubectl create -f galera-svc.yaml
$ kubectl create -f galera-secrets.yaml
$ kubectl create -f galera-statefulset.yaml
```

### Cleanup cluster
```bash
$ kubectl delete statefulset mysql -n middleware
$ kubectl delete svc galera -n middleware
$ kubectl delete pod mysql-0 mysql-1 mysql-2 -n middleware
$ kubectl delete pv datadir-mysql-0 datadir-mysql-1 datadir-mysql-2 -n middleware
```

