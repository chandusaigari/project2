 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DevOps Calculator Project</title>

<style>
    :root {
        --bg: #0b1220;
        --card: #111827;
        --text: #e5e7eb;
        --muted: #9ca3af;
        --accent: #3b82f6;
        --border: #1f2937;
    }

    body {
        font-family: "Segoe UI", Arial, sans-serif;
        margin: 0;
        background: linear-gradient(180deg, #0b1220, #0f172a);
        color: var(--text);
        line-height: 1.7;
    }

    header {
        background: rgba(17, 24, 39, 0.95);
        backdrop-filter: blur(10px);
        padding: 28px;
        text-align: center;
        border-bottom: 1px solid var(--border);
        position: sticky;
        top: 0;
        z-index: 10;
    }

    header h1 {
        margin: 0;
        font-size: 26px;
        letter-spacing: 0.5px;
    }

    .container {
        max-width: 1150px;
        margin: auto;
        padding: 30px;
    }

    section {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid var(--border);
        padding: 22px;
        margin-bottom: 25px;
        border-radius: 14px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    }

    h1, h2, h3 {
        color: var(--text);
        margin-top: 0;
    }

    h2 {
        border-left: 4px solid var(--accent);
        padding-left: 12px;
        margin-bottom: 15px;
    }

    p {
        color: var(--muted);
    }

    pre {
        background: #0a0f1c;
        color: #d1d5db;
        padding: 16px;
        border-radius: 10px;
        overflow-x: auto;
        border: 1px solid var(--border);
    }

    table {
        width: 100%;
        border-collapse: collapse;
        overflow: hidden;
        border-radius: 10px;
    }

    table, th, td {
        border: 1px solid var(--border);
    }

    th {
        background: #1f2937;
        color: white;
    }

    th, td {
        padding: 12px;
        text-align: left;
    }

    tr:hover {
        background: rgba(59, 130, 246, 0.08);
    }

    img {
        max-width: 100%;
        margin-top: 12px;
        border-radius: 12px;
        border: 1px solid var(--border);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }

    section:hover {
        border-color: rgba(59, 130, 246, 0.4);
        transition: 0.2s ease;
    }
</style>
</head>

<body>

<header>
    <h1>Project overview</h1>
</header>



<div class="container">

<section>
<p>
This project is a full-stack Calculator Web Application developed using Python, HTML, CSS, JavaScript, and MySQL. The application is integrated with a complete DevOps CI/CD pipeline using GitHub, Jenkins, Docker, Docker Hub, Kubernetes, and Argo CD.
</p>

<p>
Whenever the developer pushes code to GitHub, a webhook automatically triggers the Jenkins pipeline to build, test, and containerize the application. Docker images are pushed to Docker Hub, and Kubernetes deployments are managed through Argo CD using the GitOps approach.
</p>

<p>
The pipeline also sends automated email notifications for successful or failed builds and deployments.
</p>

<h2>Architecture</h2>

<img src="images/architecture.png" alt="Architecture Workflow" width="100%">
</section>

<section>
<h2>Tech stack</h2>

<table>
<tr><th>Category</th><th>Technology</th></tr>
<tr><td>Frontend</td><td>HTML, CSS, JavaScript</td></tr>
<tr><td>Backend</td><td>Python</td></tr>
<tr><td>Database</td><td>MySQL</td></tr>
<tr><td>CI/CD</td><td>Jenkins</td></tr>
<tr><td>Version Control</td><td>GitHub</td></tr>
<tr><td>Containerization</td><td>Docker</td></tr>
<tr><td>Container Registry</td><td>Docker Hub</td></tr>
<tr><td>Orchestration</td><td>Kubernetes</td></tr>
<tr><td>GitOps</td><td>Argo CD</td></tr>
<tr><td>Notifications</td><td>Email Extension Plugin</td></tr>
</table>
</section>

<section>
<h2>Project structure</h2>

<pre>
Project Structure

project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── Dockerfile
│
├── mysql/
│   └── init.sql
│
├── kubernetes/
│   ├── mysql-pv.yaml
│   ├── mysql-pvc.yaml
│   ├── mysql-configmap.yaml
│   ├── mysql-secrets.yaml
│   ├── mysql-deployment.yaml
│   ├── mysql-service.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   
│
├── Jenkinsfile
├── docker-compose.yml
└── README.md

</pre>
</section>

<section>
<h2>Local Setup</h2>

<h3>Jenkins Setup</h3>
<p>
Jenkins is started locally to manage CI/CD pipelines. It handles code checkout from GitHub, builds the application, runs tests, creates Docker images, and triggers deployment workflows.
</p>

<img src="images/jenkins.png" alt="Jenkins Dashboard">

<h3>Docker Setup</h3>
<p>
Docker is used to containerize backend, frontend, and database services. After installation, the Docker daemon is started to build, run, and manage containers locally before pushing images to Docker Hub.
</p>

<img src="images/docker.png" alt="Docker Running Containers">

<h2>Clone Repository</h2>

<p>To start working with the project locally, clone the source code from GitHub:</p>

<pre>git clone https://github.com/chandusaigari/project2.git</pre>

<img src="images/jenkins.png" alt="Jenkins Setup">

</section>

<section>
<h2>Backend Dockerfile</h2>

<p>
Backend Dockerfile is used to containerize the Python application. It installs required dependencies and runs the backend server inside a Docker container.
</p>

<img src="images/backend-docker.png" alt="Backend Dockerfile Build">
</section>

<section>
<h2>Frontend Dockerfile</h2>

<p>
Frontend Dockerfile is used to containerize the static web application. It serves HTML, CSS, and JavaScript files using an Nginx web server inside a container.
</p>

<img src="images/frontend-docker.png" alt="Frontend Dockerfile Build">
</section>

<section>
<h2>Jenkinsfile (CI/CD Pipeline)</h2>

<p>
Jenkinsfile defines the complete CI/CD pipeline. It automates code checkout from GitHub, builds the application, runs tests, creates Docker images, pushes them to Docker Hub, and triggers deployment to Kubernetes via Argo CD. It also sends email notifications for success or failure.
</p>

<img src="images/jenkins-pipeline.png" alt="Jenkins CI/CD Pipeline">
</section>

<section>
<h2>Docker Compose (Multi-Container Setup)</h2>

<p>
Docker Compose is used to run the full application locally with multiple containers (frontend, backend, MySQL) using a single command. It also manages shared network and persistent volume for MySQL data.
</p>

<img src="images/docker-compose.png">
</section>

<section>
<h2>Kubernetes Deployment (Complete Setup)</h2>

<p>
Kubernetes is used to deploy and manage the multi-container application (frontend, backend, MySQL). It ensures scalability, high availability, and service communication inside the cluster.
</p>

<img src="images/k8s-architecture.png">
</section>

<section>
<h2>Argo CD Application (GitOps CD)</h2>

<p>
This manifest defines the Argo CD application that continuously syncs Kubernetes manifests from GitHub and deploys updated Docker images pulled from the container registry.
</p>

<img src="images/argocd-sync.png">
</section>

<section>
<h2>GitHub Webhook</h2>

<p>
GitHub Webhook triggers Jenkins automatically whenever code is pushed or any change is made in the repository. This starts the CI/CD pipeline without manual intervention.
</p>

<img src="images/github-webhook.png">
</section>

<section>
<h2>Email Notifications</h2>

<p>
After every Jenkins pipeline run, an email notification is sent automatically based on the result.
If the build and deployment are successful, a success email is sent. If any stage fails, a failure email is sent.
</p>

<img src="images/email-success-failure.png">
</section>

<section>
<h2>Docker Hub Images</h2>

<p>
After a successful Jenkins pipeline execution, the Docker images are automatically pushed to Docker Hub registry.
</p>

<img src="images/dockerhub-images.png">
</section>

<section>
<h2>Kind Cluster Setup (Kubernetes)</h2>

<p>
Kind is used to create a local Kubernetes cluster for testing and deployment of the application.
</p>

<pre>
kind create cluster --name calculator-cluster
kubectl get nodes
</pre>

<img src="images/kind-cluster.png">
</section>

<section>
<h2>Namespace Creation</h2>

<pre>
kubectl apply -f ns.yaml
kubectl get namespaces
</pre>

<img src="images/namespace-created.png">
</section>

<section>
<h2>Argo CD Setup</h2>

<pre>
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl get pods -n argocd
kubectl get pods -n argocd -w
</pre>

<img src="images/argocd-pods-running.png">
</section>

<section>
<h2>Port Forwarding</h2>

<pre>
kubectl port-forward svc/argocd-server -n argocd 8080:443
https://localhost:8080

kubectl port-forward svc/backend-service -n calculator 5000:5000
http://localhost:5000

kubectl port-forward svc/frontend-service -n calculator 80:80
http://localhost:80

kubectl port-forward svc/mysql-service -n calculator 3306:3306
localhost:3306
</pre>
</section>

<section>
<h2>MySQL Data Verification</h2>

<pre>
kubectl exec -it &lt;mysql-pod-name&gt; -n e-ns -- mysql -u root -p

SHOW DATABASES;
USE appdb;
SHOW TABLES;
SELECT * FROM calculations;
</pre>

<img src="images/mysql-data-check.png">
</section>

</div>

</body>
</html>
