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

# Deploy KEDA scaledobject
echo "Deploying Scaled Object..."
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
helm install keda kedacore/keda --namespace keda --create-namespace
kubectl apply -f "$MANIFEST_DIR/scaledobject-deployment.yaml"


# Deploy Dapr PubSub Component
echo "Deploying Dapr PubSub Component..."
kubectl apply -f "$MANIFEST_DIR/pubsub-component.yaml" 

# Declarative Subscriptions
echo "Deploying subscriptions Component..."
kubectl apply -f "$MANIFEST_DIR/subscriptions.yaml" 


# Deploy Publisher Service
echo "Deploying Publisher Service..."
kubectl apply -f "$MANIFEST_DIR/publisher-deployment.yaml"

# Deploy Reconstruct Service
echo "Deploying Reconstruct Service..."
kubectl apply -f "$MANIFEST_DIR/reconstruct-deployment.yaml"

# Deploy SAR Processor Service
echo "Deploying SAR Processor Service..."
kubectl apply -f "$MANIFEST_DIR/sarprocessor-deployment.yaml"

# Deploy Vesseldetector Service
echo "Deploying Vesseldetector Service..."
kubectl apply -f "$MANIFEST_DIR/vesseldetector-deployment.yaml"

# Set up subscriptions
kubectl apply -f "$MANIFEST_DIR/subscriptions.yaml"

echo "All components have been deployed."
