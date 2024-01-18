# pubsub-demo
Demo of a microservice application using dapr and kubernetes.

Requirements:
 - Docker Desktop with kubernetes installed
 - kubectl cli
 - helm
 - k9s(optional for viewing k8s pods)


Edit the "MANIFEST_DIR" variable in the build_images.sh script mathch the location of the /deployment folder on your pc

To deploy the system, first run:

```
./build_images.sh
```

Then:

```
./deploy.sh
```

To view running pods, open k9s or inspect running containers in Docker Desktop.
