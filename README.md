## Requirements
- Kubernetes 1.3+

Tested on Kubernetes v1.21.3

To operate a MariaDB Galera Cluster on top of Kubernetes it is especially important to implement the bootstrap of the cluster and to construct the configuration based on the current pods in the PetSet. In our case those tasks are taken care of by two init containers. In the galera-init image the tools to perform the bootstrap are packaged, and a second container runs the peer-finder binary, which queries the SRV record of the assigned service and generates the configuration for the MariaDB Galera Cluster based on the current members of the PetSet.

When the first statefulset starts, wsrep_cluster_address=gcomm:// is used and the pod automatically bootstraps the cluster. Subsequently started sets add the hostnames they receive from the SRV record to wsrep_cluster_address and automatically join the cluster. Below is an example of what the configuration would look like after the start of the second statefulset.

## Create SRV record
for example a simple SRV config in dnsmasq would be

srv-host=galera,mysql-0.galera.middleware.svc.cluster.local,3306,1

/etc/hosts

For minikube e.g.
172.17.0.2      mysql-0 mysql-0.galera.middleware.svc.cluster.local
For worker e.g.
10.44.0.2      mysql-0 mysql-0.galera.middleware.svc.cluster.local

Bootstrap the cluster with a single mysql node and once up and running, then add the remaining 2 SRV records to create a 3 node galera cluster.


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

Make sure of necessary permissions on the local disk under volume path for container to read/write into it.

### Cleanup cluster
```bash
$ kubectl delete statefulset mysql -n middleware
$ kubectl delete svc galera -n middleware
$ kubectl delete pod mysql-0 mysql-1 mysql-2 -n middleware
$ kubectl delete pv datadir-mysql-0 datadir-mysql-1 datadir-mysql-2 -n middleware
```

