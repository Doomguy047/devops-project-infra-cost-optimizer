# Infrastructure Cost Optimizer

Student Name: NAMAN JAIN  
Registration No: 23FE10CSE00031  
Course: DevOps  
Difficulty: Intermediate  

---

## Project Overview

### Problem Statement

Cloud environments often contain underutilized or misconfigured resources that increase operational cost.  
This project simulates a cloud infrastructure cost optimizer that analyzes infrastructure data and provides cost-saving recommendations.

---

## Objectives

- Analyze simulated cloud infrastructure data
- Detect cost inefficiencies
- Provide optimization recommendations
- Automate build and testing using CI/CD
- Containerize the application using Docker

---

## Key Features

- EC2 utilization analysis
- EBS unattached volume detection
- S3 lifecycle and public access checks
- HTML cost optimization report generation
- Dockerized deployment
- GitHub Actions CI pipeline

---

## Technology Stack

### Core Technologies
- Programming Language: Python 3.11
- Data Format: JSON

### DevOps Tools
- Version Control: Git
- CI/CD: GitHub Actions
- Containerization: Docker
- OS: macOS (Apple Silicon M1)

---

## Getting Started

### Prerequisites
- Docker Desktop
- Git

### Run Locally

```bash
cd src/main
python3 app.py
```

Output:
Cost analysis complete. Report generated: cost-report.html

---

### Run Using Docker

Build Docker image:

```bash
docker build -t infra-cost-optimizer -f infrastructure/docker/Dockerfile .
```

Run container:

```bash
docker run -v $(pwd)/src/main:/app infra-cost-optimizer
```

The report will be generated inside:
src/main/cost-report.html

---

## Project Structure

```
devops-project-infra-cost-optimizer/
│
├── src/main/
│   ├── app.py
│   ├── cost_engine.py
│   ├── rules.py
│   ├── report_generator.py
│   └── sample_data.json
│
├── infrastructure/docker/
│   └── Dockerfile
│
├── .github/workflows/
│   └── ci-cd.yml
│
├── README.md
└── requirements.txt
```

---

## Optimization Rules Implemented

### EC2
- CPU usage < 10% → Suggest downsizing
- Stopped instances → Suggest termination

### EBS
- Unattached volumes → Suggest deletion

### S3
- No lifecycle policy → Suggest configuration
- Public bucket → Security and cost warning

---

## CI/CD Pipeline

The GitHub Actions pipeline automatically:

1. Checks out the repository
2. Sets up Python environment
3. Runs the cost analysis application
4. Builds the Docker image

The pipeline is triggered on every push to the `main` branch.

This demonstrates Continuous Integration.

---

## Output

The system generates:

- cost-report.html

This file contains infrastructure cost optimization recommendations.

---

## Future Enhancements

- Integration with real AWS APIs (Boto3)
- Real-time cost estimation metrics
- Dashboard visualization interface
- Scheduled automated scans
- Multi-cloud support

---

## Learnings

- Implemented DevOps lifecycle
- Built automated CI pipeline
- Containerized application using Docker
- Applied infrastructure cost governance concepts

---

## Conclusion

This project demonstrates how DevOps practices can be applied to infrastructure cost management through automation, containerization, and continuous integration.
