#!/bin/bash


IMAGE_TAG="$1"
echo "Reverting to TAG $1"

#git Branch
# AWS details
AWS_ACCOUNT_ID="559615561845"
AWS_REGION="ap-south-1"
ECR_REPO_NAME="devops-scripts"


# Authenticate Docker with ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

echo "ECR Login Succeeded"

export DOCKER_IMAGE_NAME=superset-$IMAGE_TAG
# Tag the Docker image with ECR repository details
export DOCKER_IMAGE_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME"

echo "Restarting SuperSet"
docker compose down --timeout 10

docker compose -f docker-compose-custom.yml up -d

echo "Revert Complete, TAG $1 has been deployed successfuly"
set +e
