#!/bin/bash
MANIFEST_DIR="/Users/havardg/PycharmProjects/pubsub-demo/deployment"

echo "Starting Kubernetes deployments..."

kubectl config set-context --current --namespace=default

# Deploy dapr
helm repo add dapr https://dapr.github.io/helm-charts/
helm repo update
# See which chart versions are available
helm search repo dapr --devel --versions
helm upgrade --install dapr dapr/dapr \
--version=1.6 \
--namespace dapr-system \
--create-namespace \
--wait

# Deploy Redis
echo "Deploying Redis..."
kubectl apply -f "$MANIFEST_DIR/redis-deployment.yaml"
kubectl apply -f "$MANIFEST_DIR/redis-service.yaml"


# Deploy Dapr PubSub Component
echo "Deploying Dapr PubSub Component..."
kubectl apply -f "$MANIFEST_DIR/pubsub-component.yaml" 

# Declarative Subscriptions
echo "Deploying subscriptions Component..."
kubectl apply -f "$MANIFEST_DIR/subscriptions.yaml" 


echo "All components have been deployed."
