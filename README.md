# CI/CD Pipeline: Build, Push, and Update Deployment

This repository includes a GitHub Actions workflow to automate building, pushing, and deploying Docker images based on changes to the `main` branch.

## 📦 Workflow Overview

The GitHub Actions pipeline performs the following steps:

1. **Trigger**: Runs on push or pull request to the `main` branch, and can be manually triggered via `workflow_dispatch`.
2. **Checkout Code**: Fetches the repository.
3. **Docker Setup**: Prepares Docker Buildx for advanced builds.
4. **Login to DockerHub**: Authenticates using secrets.
5. **Get Model Version**: Detects the latest model version from the `models/` directory.
6. **Build & Push Image**: Builds the Docker image using the model version and pushes both `:latest` and version-specific tags to DockerHub.
7. **Update Kubernetes Deployment**: Updates `k8s/deployment.yaml` with the new Docker image tag.
8. **Commit Deployment File Change**: Automatically commits the updated deployment file back to the repo.

## 🖼️ Pipeline Flow

![Pipeline Flow](./images/pipeline_flow.png)

## 🛠️ Secrets Required

Make sure the following GitHub secrets are set in your repository:

- `DOCKERHUB_USERNAME` — Your Docker Hub username
- `DOCKERHUB_TOKEN` — A Docker Hub access token or password

## 🐳 Docker Image Info

Images are built and pushed to:

