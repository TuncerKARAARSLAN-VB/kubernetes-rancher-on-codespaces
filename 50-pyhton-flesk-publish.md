To run a Python application on Minikube, you'll follow a series of steps that involve setting up your Minikube environment, creating a Docker image for your Python application, and deploying that image to Minikube. 

### Step 1: Start Minikube

1. **Open your terminal** and start Minikube:
   ```bash
   minikube start
   ```

2. **Verify the status** of Minikube:
   ```bash
   minikube status
   ```

### Step 2: Create a Simple Python Application

1. **Create a directory for your application**:
   ```bash
   mkdir my-python-app
   cd my-python-app
   ```

2. **Create a Python file** (e.g., `app.py`):
   ```python
   # app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello_world():
       return 'Hello, World!'
   
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=8080)
   ```

3. **Create a requirements file** (`requirements.txt`) for dependencies:
   ```
   Flask==2.1.2
   ```

### Step 3: Create a Dockerfile

1. **Create a `Dockerfile`** in the same directory:
   ```dockerfile
   # Dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt
   COPY . .
   
   CMD ["python", "app.py"]
   ```

### Step 4: Build the Docker Image

1. **Set the Docker environment to Minikube**:
   ```bash
   eval $(minikube docker-env)
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t my-python-app .
   ```

### Step 5: Create a Kubernetes Deployment

1. **Create a Kubernetes deployment file** (`deployment.yaml`):
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: my-python-app
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: my-python-app
     template:
       metadata:
         labels:
           app: my-python-app
       spec:
         containers:
         - name: my-python-app
           image: my-python-app
           ports:
           - containerPort: 8080
   ```

2. **Apply the deployment**:
   ```bash
   kubectl apply -f deployment.yaml
   ```

### Step 6: Expose the Application

1. **Expose the deployment to access it externally**:
   ```bash
   kubectl expose deployment my-python-app --type=NodePort --port=8080
   ```

2. **Get the URL to access your app**:
   ```bash
   minikube service my-python-app --url
   ```

### Step 7: Access Your Application

- Open your browser and navigate to the URL obtained from the previous command. You should see "Hello, World!" displayed.

    This command provides dev environment port and ip information  
   ```bash
    minikube -p minikube docker-env
   ```

### Conclusion

You have successfully set up a simple Python application running in Minikube. You can now develop and test more complex applications using this setup.