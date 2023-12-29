#!/bin/bash
MANIFEST_DIR="/Users/havardhanssen/projects/work/pubsub-demo/deployment"

echo "Starting Kubernetes deployments..."

# Deploy helkeda
helm install keda kedacore/keda --namespace keda --create-namespace


# Deploy Redis
echo "Deploying Redis..."
kubectl apply -f "$MANIFEST_DIR/redis-deployment.yaml"

# Deploy scaledobject
echo "Deploying Scaled Object..."
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

# Deploy Vesseldetector Service
echo "Deploying Vesseldetector Service..."
kubectl apply -f "$MANIFEST_DIR/vesseldetector-deployment.yaml"

echo "All components have been deployed."
