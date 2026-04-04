# ACEest Fitness DevOps Assignment

## Setup

pip install -r requirements.txt  
python app.py

## Run Tests

pytest

## Docker

docker build -t aceest-app .  
docker run -p 5000:5000 aceest-app

## CI/CD

GitHub Actions pipeline runs on every push:
- Install dependencies
- Run tests
- Build Docker image

## Jenkins

Jenkins is configured to pull from GitHub and run tests as part of build validation.
