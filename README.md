# ACEest Fitness DevOps Assignment

This project implements a gym management backend service using Flask and demonstrates a complete DevOps workflow including testing, containerization, continuous integration, and deployment using modern tools and practices.

---

## Application Overview

The application provides APIs for managing gym-related operations such as:

* User login
* Client management
* Workout tracking
* Basic metrics recording

The backend is developed using Flask and uses SQLite for data storage.

---

## Local Setup and Execution

### 1. Clone the repository

git clone https://github.com/2024tm93539-dev/ACEest-fitness.git
cd ACEest-fitness

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the application

python app.py

The application runs on:

http://localhost:5001

---

## Unit Testing with Pytest

Automated unit tests are implemented using Pytest to validate API functionality and application behavior.

Run tests using:

pytest

---

## Docker Containerization

The application is containerized using Docker to ensure consistent runtime environments.

### Build Docker Image

docker build -t aceest-fitness:v1 .

### Run Docker Container

docker run -p 5001:5001 aceest-fitness:v1

---

## CI/CD Pipeline

The project follows a hybrid CI/CD approach using GitHub Actions and Jenkins.

### GitHub Actions

* Automatically triggered on every push and pull request
* Installs dependencies
* Executes Pytest test cases
* Builds Docker image

### Jenkins

* Pulls latest code from GitHub
* Installs dependencies
* Runs test cases using Pytest
* Builds Docker image

This ensures continuous integration and validation of the application.

---

## Kubernetes Deployment

The application is deployed using Kubernetes to ensure scalability and high availability.

### Components:

* Deployment: Manages application replicas
* Service: Exposes the application using NodePort

Kubernetes configuration files are available in the `k8s/` directory.

---

## Deployment Strategies

The following deployment strategies are incorporated:

* Rolling Update: Gradual update of application instances
* Blue-Green Deployment: Separate environments for zero-downtime switching
* Canary Deployment: Gradual rollout to a subset of users
* A/B Testing: Comparing multiple versions
* Shadow Deployment: Testing new versions alongside production

Blue and Green deployment configurations are available in the `k8s/` directory.

---

## Project Structure

* app.py → Flask application
* test_app.py → Pytest test cases
* requirements.txt → Dependencies
* Dockerfile → Container configuration
* Jenkinsfile → CI pipeline definition
* k8s/ → Kubernetes manifests
* .github/workflows/main.yml → GitHub Actions pipeline
* README.md → Documentation

---

## Summary

This project demonstrates:

* Version control using Git and GitHub
* Automated testing using Pytest
* Continuous integration using GitHub Actions and Jenkins
* Containerization using Docker
* Deployment using Kubernetes
* Implementation of modern deployment strategies

The overall implementation reflects a complete DevOps pipeline ensuring reliability, scalability, and efficient software delivery.
