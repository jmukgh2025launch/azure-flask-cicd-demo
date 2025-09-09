# Azure Flask CI/CD Demo

Demo project: containerized Flask app with CI via Azure DevOps.

- Build: Docker
- Test: pytest
- CI: Azure DevOps pipeline pushes image to Docker Hub and runs a smoke test

## To run locally
1. `pip install -r requirements.txt`
2. `pytest`
3. `docker build -t flask-demo:local .`
4. `docker run -p 5000:5000 flask-demo:local`
