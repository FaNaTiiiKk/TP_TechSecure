# 🛡️ TechSecure Solutions - Secure Subsidiary Management

A containerized web application designed to centralize and secure the management of company subsidiaries (Paris, Lyon, Marseille). This project focuses on application-level security, robust error handling, and infrastructure isolation as part of a secure professional deployment.

---

## ✨ Features

- **Subsidiary Management**: Centralized CRUD dashboard replacing insecure local Excel files.
- **Secure Database Interfacing**: Strict usage of parameterized queries to completely eliminate SQL Injection risks.
- **Fail-Safe Error Management**: Global exception masking using Flask's `flash` system to prevent sensitive system info leaks.
- **Cryptographic Readiness**: Full integration of `bcrypt` with dynamic salting for industry-standard password hashing.
- **Containerized Stack**: Complete infrastructure (Flask, MySQL) orchestrated seamlessly via Docker Compose.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Database**: MySQL 8.0 (Isolated)
- **Frontend**: HTML5, CSS3 (Responsive Design with modern dark-blue theme)
- **Security**: Bcrypt Cryptography
- **Infrastructure**: Docker, Docker Compose

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have **Docker** and **Docker Compose** installed and running on your machine (Windows, Mac, or Linux).

### 2. Installation & Deployment

Clone the project or navigate to the repository directory:
```bash
cd TP_TechSecure
```
Build and launch the infrastructure in detached mode:

```Bash
docker compose up --build -d
```
(Note: The --build flag ensures that all updated dependencies, including the bcrypt library, are freshly installed inside the container).

3. Accessing the Application
Once the containers are up and running, open your preferred web browser and go to:
👉 http://localhost:5000

🔒 Applied Security Policies (Audit Compliant)
The architecture and source code have been hardened according to corporate security guidelines:

SQL Injection Prevention: Concat-based queries are forbidden. All database interactions utilize SQL parameters (%s).

Information Exposure Mitigation: Raw Python/MySQL exceptions (try/except blocks) are masked from end-users, neutralizing infrastructure footprinting attempts.

Network Isolation: The MySQL database container is confined strictly to Docker's internal network. Port 3306 is closed to the host machine, blocking external brute-force vectors.

Data Validation: Strict server-side verification of mandatory form inputs before hitting the persistence layer.

```text
📁 Project Structure
Plaintext
TP_TechSecure/
├── app.py              # Main Flask application, secured routes & error handling
├── requirements.txt    # Python dependencies (Flask, mysql-connector, bcrypt)
├── docker-compose.yml  # Service, network and volume orchestration
├── static/             # Assets (Custom CSS styles, corporate images)
│   ├── CSS/
│   │   └── style.css   # Main stylesheet (Modern corporate theme)
│   └── IMAGE/          # Local subsidiary and corporate graphics
└── templates/          # Secured Jinja2 HTML templates (base, accueil, filiales, etc.)
```

🌐 Repository Link

Official GitHub Repository: https://github.com/FaNaTiiiKk/TP_TechSecure.git