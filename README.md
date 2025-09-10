# Project goal:

### Containerized Flask app with a fully automated CI/CD pipeline in Azure DevOps, demonstrating modern cloud engineering practices

This project's goal was to demonstrate a complete CI/CD pipeline for a containerized Python Flask application using Azure DevOps.

The goal was to showcase cloud engineering and DevOps practices without relying on paid cloud services.

The app is built and tested locally with Docker, unit-tested with pytest, and automatically packaged into a Docker image.

Through the Azure DevOps pipeline, the image is pushed to Docker Hub and smoke-tested to ensure functionality.

This setup highlights skills in containerization, automated testing, pipeline design, and secure secret management, while remaining fully reproducible on free tiers.

#### Flask API → Dockerized → tested with pytest → built & published via Azure DevOps pipelines → deployment-ready artifact

# Progress:

A request was put into Microsoft to grant free parellelism in order to re-run the failed pipeline, but so far this request has not been granted.

### Project Recap:
1. Created GitHub repo with Flask app, Dockerfile, tests, and pipeline YAML
2. Set up Azure DevOps project and connected it to GitHub
3. Added .azure-pipelines/azure-pipelines.yml and triggered first run
4. Pipeline failed due to no hosted parallelism
5. Submitted Microsoft’s parallelism request form
6. Tried making project public → blocked by school tenant policy
7. Added Docker Hub secrets in Azure DevOps and updated pipeline YAML
8. Safely paused VS Code work (all changes pushed to GitHub)

### Issues & Solutions:
- No hosted parallelism → Submitted Microsoft free parallelism request
- Couldn’t make project public → Blocked by school’s tenant policy
- Workarounds → Wait for approval, use personal MS account, or run self-hosted agent

### Remaining Steps:
1. Get parallelism working (approval or self-hosted)
2. Run pipeline successfully (tests → Docker build → push to Docker Hub → smoke test)
3. Confirm Docker Hub image
4. Polish repo (status badge, README updates)
