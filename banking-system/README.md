# Banking System API

This document provides a quick reference for setting up and running the **Banking System API**.

## Requirements

Make sure the following are installed on your system:
- Docker and Docker Compose
- Python 3.10+
- Pip (Python package manager)

## Steps to Run the Project

### 1. Clone the Repository

Clone the project repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>

### 2. Run Project

Using Docker
```bash
docker-compose up -d --build

Running Locally Without Docker
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
