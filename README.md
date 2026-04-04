# ACEest Fitness DevOps Assignment

This project implements a simple gym management backend service using Flask and demonstrates a complete DevOps workflow including testing, containerization, and CI/CD pipelines.

---

## 📌 Application Overview

The application provides basic APIs for managing gym-related data such as:

- User login
- Client management
- Workout tracking
- Basic metrics recording

The backend is built using Flask and uses SQLite for data storage.

---

## ⚙️ Local Setup & Execution

### 1. Clone the repository

git clone https://github.com/2024tm93539-dev/ACEest-fitness.git  
cd ACEest-fitness

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the application

python app.py

The application will run on:

http://localhost:5001

---

## 🧪 Running Tests

To execute unit tests using Pytest:

pytest

This validates:
- API endpoints
- Request handling
- Basic application logic

---

## 🐳 Docker Setup

### Build the Docker image

docker build -t aceest-app .

### Run the container

docker run -p 5001:5001 aceest-app

---

## 🔄 CI/CD Pipeline (GitHub Actions)

GitHub Actions is configured to automatically run on every push and pull request.

### Pipeline Stages:
1. Install dependencies
2. Run Pytest test suite
3. Build Docker image

This ensures that:
- Code changes do not break functionality
- Application is always build-ready

---

## 🏗️ Jenkins Build Integration

Jenkins is used as a secondary build validation tool.

### Workflow:
- Jenkins pulls the latest code from GitHub
- Executes a basic build validation step
- Confirms repository structure and readiness

GitHub Actions handles testing and containerization, while Jenkins acts as an additional validation layer in the pipeline.

---

## 📁 Project Structure

- app.py → Flask application
- test_app.py → Pytest test cases
- requirements.txt → Dependencies
- Dockerfile → Container configuration
- .github/workflows/main.yml → CI/CD pipeline
- README.md → Documentation

---

## ✅ Summary

This project demonstrates:
- Version control using Git and GitHub
- Automated testing using Pytest
- Containerization using Docker
- CI/CD using GitHub Actions
- Build validation using Jenkins

