#!/bin/bash
MANIFEST_DIR="/Users/havardhanssen/projects/work/pubsub-demo/deployment"

echo "Starting Kubernetes deployments..."

# Deploy Redis
echo "Deploying Redis..."
kubectl apply -f "$MANIFEST_DIR/redis-deployment.yaml"

# Deploy Dapr PubSub Component
echo "Deploying Dapr PubSub Component..."
kubectl apply -f "$MANIFEST_DIR/pubsub-component.yaml" 

# Deploy Publisher Service
echo "Deploying Publisher Service..."
kubectl apply -f "$MANIFEST_DIR/publisher-deployment.yaml"

echo "All components have been deployed."
