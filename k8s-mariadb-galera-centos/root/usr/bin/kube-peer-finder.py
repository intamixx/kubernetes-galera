!/usr/bin/python3

from kubernetes import client, config, watch
import sys

# Configs can be set in Configuration class directly or using helper utility
#config.load_kube_config()
config.load_incluster_config()

try:
    namespace = sys.argv[1]
except:
    print ("Require the first argument to be namespace")
    sys.exit(1)

v1 = client.CoreV1Api()
#print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    if (i.metadata.namespace == namespace):
#           print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
            print("%s\t%s" % (i.status.pod_ip, i.metadata.name))


sys.exit(0)
