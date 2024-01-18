# pubsub-demo
Demo of a microservice application using dapr and kubernetes.

Requirements:
 - Docker Desktop with kubernetes installed
 - kubectl cli
 - helm


Edit the "MANIFEST_DIR" variable in the build_images.sh script mathch the location of the /deployment folder on your pc

To deploy the system, first run:

```
./build_images.sh
```

Then:

```
./deploy.sh
```
