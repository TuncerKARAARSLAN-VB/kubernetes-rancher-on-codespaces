# How to install developer app into pod

To "push" an application developed into a Kubernetes Pod, you typically follow these steps. These steps include creating your application as a Docker image, uploading that image to a container registry, and then using that image to create a Pod in Kubernetes.

## Step 1: Create a Docker Image for Your Application

1. **Create a Dockerfile**: Create a `Dockerfile` in the directory where your application is located. Here’s an example of a `Dockerfile`:

   ```dockerfile
   # Base image
   FROM python:3.9-slim

   # Working directory
   WORKDIR /erdem-helloworld

   # Copy requirements file and application files
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .

   # Start the application
   CMD ["python", "app.py"]
   ```

2. **Build the Docker Image**: Run the following command in the terminal to build your Docker image:

   ```bash
   docker build -t your-username/your-app-name:latest .
   ```

   Replace `your-username/your-app-name` with your own username and application name.

## Step 2: Push the Docker Image to a Registry

Follow these steps to upload your Docker image to a container registry (for example, Docker Hub):

1. **Login to Docker Hub**: If you're using Docker Hub, you need to log in first:

   ```bash
   docker login
   ```

2. **Push the Image**: Use the following command to upload your created image:

   ```bash
   docker push your-username/your-app-name:latest
   ```

## Step 3: Create a Kubernetes Pod

Now that your Docker image is uploaded to the registry, you can create a Kubernetes Pod using that image.

1. **Create a YAML File**: Create a YAML file that defines a Pod for your application. Here’s a simple example:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: your-app-pod
   spec:
     containers:
     - name: your-app-container
       image: your-username/your-app-name:latest
       ports:
       - containerPort: 80
   ```

2. **Create the Pod**: Use the YAML file to create the Pod:

   ```bash
   kubectl apply -f your-app-pod.yaml
   ```

## Step 4: Check the Pod Status

You can check whether the Pod was created successfully by using the following command:

```bash
kubectl get pods
```

## Summary

The steps above summarize how to "push" an application developed into a Kubernetes Pod. You create your application as a Docker image, upload that image to a registry, and then create a Pod in Kubernetes using that image.