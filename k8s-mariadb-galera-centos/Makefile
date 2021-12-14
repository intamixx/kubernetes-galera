IMAGE_NAME=intamixx/kubernetes-galera
IMAGE_VERSION=latest
LOCAL_REGISTRY=localhost:5000

image:
	docker build -t $(IMAGE_NAME):$(IMAGE_VERSION) .

push:
	docker tag $(IMAGE_NAME):$(IMAGE_VERSION) $(LOCAL_REGISTRY)/$(IMAGE_NAME):$(IMAGE_VERSION)
	docker push $(LOCAL_REGISTRY)/$(IMAGE_NAME):$(IMAGE_VERSION)
