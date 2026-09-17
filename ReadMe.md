Cloud Healing Project
Secure Self-Healing Cloud Infrastructure

A lightweight project that demonstrates a self-healing cloud application built with Python, Flask, Docker, Prometheus, and Kubernetes. The application exposes health and metrics endpoints, while an automated monitoring script detects failures and restarts the service when required.

Overview

This repository implements a simplified cloud resilience workflow:

A Flask web application serves HTTP requests and exposes monitoring endpoints.
Prometheus scrapes metric data from the application.
Docker Compose runs the application and monitoring stack locally.
Kubernetes manifests provide a deployment path for container orchestration.
A Python self-healing script periodically checks application health and restarts the container if failures are detected.
Architecture

The basic workflow is:

The Flask application runs on port 5000.
/health returns the application's health status.
/metrics exposes Prometheus-compatible metrics.
Prometheus scrapes the application at regular intervals.
A monitoring script continuously checks the health endpoint.
If the application fails repeatedly, the script triggers a Docker container restart.
Repository Structure
cloud-healing-project/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── automation/
│   ├── alerts.log
│   └── healing_script.py
├── monitoring/
│   └── prometheus.yml
├── deployment.yaml
├── docker-compose.yml
├── service.yaml
├── index.html
├── aws.html
├── docker.html
├── flask.html
├── grafana.html
├── kubernetes.html
├── prometheus.html
├── python.html
├── compose.html
├── tech-shared.css
├── install.cmd
├── CloudHeal_Presentation.pptx
├── README.md
└── LICENSE
Application

The main application is implemented in:

app/app.py
Endpoints
Endpoint	Description
/	Returns a welcome message
/health	Returns the application health status
/metrics	Exposes Prometheus-compatible metrics
Example Health Response
{
  "status": "healthy"
}

The application tracks:

Total request count
Request latency
Prometheus metrics for monitoring and alerting
Monitoring and Metrics

Prometheus is configured in:

monitoring/prometheus.yml

The key scrape configuration is:

scrape_configs:
  - job_name: 'healing-app'
    static_configs:
      - targets: ['healing-app:5000']
    metrics_path: '/metrics'

This allows Prometheus to collect application metrics for monitoring and enables visualization through Prometheus and Grafana.

Self-Healing Automation

The self-healing script is located at:

automation/healing_script.py

The script continuously checks the application's health.

It:

Sends requests to http://localhost:5000/health
Logs alert information to automation/alerts.log
Tracks repeated health-check failures
Restarts the Docker container when the application becomes unhealthy

This demonstrates the concept of automated recovery and self-healing in a cloud environment.

Local Deployment with Docker Compose
Prerequisites

Make sure the following are installed:

Docker
Docker Compose
Python 3
Start the Stack
docker compose up --build
Access the Services
Service	URL
Application	http://localhost:5000/
Health Endpoint	http://localhost:5000/health
Prometheus	http://localhost:9090/
Grafana	http://localhost:3000/
Stop the Stack
docker compose down
Kubernetes Deployment

A Kubernetes deployment manifest is included in:

deployment.yaml

The deployment defines:

3 replicas
Container port 5000
Liveness probe on /health
Readiness probe on /health
Deploy to Kubernetes
kubectl apply -f deployment.yaml

If a Kubernetes service manifest is also required, apply:

kubectl apply -f service.yaml
Dependencies

Application dependencies are listed in:

app/requirements.txt
Flask
prometheus_client
requests
Run the Self-Healing Script

From the project root:

python automation/healing_script.py

The script runs continuously and monitors the health of the application.

Project Workflow
                 ┌──────────────────┐
                 │   Flask App      │
                 │    Port 5000     │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        /health Endpoint        /metrics Endpoint
              │                       │
              ▼                       ▼
      Self-Healing Script          Prometheus
              │                       │
              │                       ▼
              │                    Grafana
              │
              ▼
       Docker Restart
Notes

This repository is intended as a demonstration of:

Cloud resilience
Application monitoring
Health checks
Containerization
Kubernetes orchestration
Prometheus metrics
Automated self-healing

The project is intentionally lightweight and can be extended with:

Stronger alerting workflows
External monitoring integrations
Centralized log aggregation
Production-oriented orchestration
Advanced failover mechanisms
Cloud-based deployment
Automated incident notification
License

This repository currently does not include an explicit license file.

If you plan to reuse or distribute this project, add a license that matches your intended usage.

Contributing

Contributions are welcome.

You can improve the project by enhancing:

Deployment logic
Monitoring and observability
Self-healing automation
Kubernetes configurations
Logging and alerting

For changes, open a pull request with a clear description of the improvements.