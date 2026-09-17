# ☁️ CloudHeal — Secure Self-Healing Cloud Infrastructure

<p align="center">

  <img src="https://img.shields.io/badge/Cloud-Self--Healing-blue?style=for-the-badge&logo=icloud&logoColor=white" alt="Cloud Self Healing">

  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python">

  <img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">

  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">

  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes">

  <img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus">

  <img src="https://img.shields.io/badge/Grafana-Observability-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana">

</p>

<p align="center">
  <b>Detect → Monitor → Heal → Recover</b>
</p>

<p align="center">
  A lightweight cloud-native project demonstrating automated failure detection,
  application monitoring, container recovery, and Kubernetes-based resilience.
</p>

---

## 🚀 Project Overview

**CloudHeal** is a Secure Self-Healing Cloud Infrastructure project designed to demonstrate how a cloud application can detect failures and automatically recover with minimal manual intervention.

The project combines:

- 🐍 **Python & Flask** for the application layer
- 🐳 **Docker** for containerization
- 📊 **Prometheus** for metrics collection
- 📈 **Grafana** for observability
- ☸️ **Kubernetes** for container orchestration
- 🔄 **Python automation** for health monitoring and recovery
- 📝 **Logging** for tracking healing events

The core idea is simple:

> **When the application becomes unhealthy, the infrastructure should be able to detect the problem and take corrective action automatically.**

---

# 🎯 Why Self-Healing?

Traditional applications often depend on a human operator to:

1. Detect that an application has failed
2. Identify the affected service
3. Investigate the failure
4. Restart the service
5. Verify that the service has recovered

CloudHeal demonstrates a different approach:

```text
                 ┌──────────────────────┐
                 │     Flask App         │
                 │      Port 5000        │
                 └──────────┬───────────┘
                            │
                 ┌──────────▼───────────┐
                 │     Health Check      │
                 │       /health         │
                 └──────────┬───────────┘
                            │
                     Healthy?
                       /       \
                     YES       NO
                      │         │
                      ▼         ▼
                 Continue    Healing
                 Service     Automation
                                │
                                ▼
                         Restart Container
                                │
                                ▼
                         Service Recovery
