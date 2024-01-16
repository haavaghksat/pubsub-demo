#!/bin/zsh

# Directory containing all projects
SRC_DIR="/Users/havardg/PycharmProjects/pubsub-demo/src"

PREV_DIR=$(pwd)  # Save the current directory

# Iterate over each subdirectory in /src
for dir in "$SRC_DIR"/*; do
  if [ -d "$dir" ]; then
    # Get the name of the directory
    PROJECT_NAME=$(basename "$dir")
    # Change to the project directory
    cd "$dir" || continue
    # Check if Dockerfile exists in the directory
    if [ -f "Dockerfile" ]; then
      echo "Building Docker image for $PROJECT_NAME..."

      # Build the Docker image
      # Tag the image with the name of the directory
      docker build -t "$PROJECT_NAME":latest .

      echo "$PROJECT_NAME image built successfully"
    else
      echo "No Dockerfile found in $PROJECT_NAME, skipping..."
    fi
    # Return to the previous directory
    cd "$PREV_DIR" || exit
  fi
done
