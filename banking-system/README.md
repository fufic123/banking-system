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

<code>git clone &lt;repository-url&gt;</code>

Change to the project directory:

<code>cd &lt;repository-directory&gt;</code>

### 2. Run Project

#### Using Docker

Build and run the project with Docker Compose:

<code>docker-compose up -d --build</code>

#### Running Locally Without Docker

Create a virtual environment:

<code>python -m venv venv</code>

Activate the virtual environment:

On Linux/macOS:
<code>source venv/bin/activate</code>

On Windows:
<code>venv\Scripts\activate</code>

Install the required dependencies:

<code>pip install -r requirements.txt</code>

Run the application:

<code>uvicorn main:app --reload</code>
