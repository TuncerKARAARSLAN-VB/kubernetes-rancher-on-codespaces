# How to update new pod

To replace an old Pod with a new one in Kubernetes, you typically follow an update or redeployment process. This process may vary depending on the specific application deployment method you are using. Here are the steps on how to do this:

## 1. Update Using a Deployment

The most common method is to use a **Deployment** to manage updates. This simplifies version control for your Pods.

### Step 1: Update the Deployment YAML File

If you have an existing Deployment, update the YAML file to specify the new image version. For example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: your-app
  template:
    metadata:
      labels:
        app: your-app
    spec:
      containers:
      - name: your-app-container
        image: your-username/your-app-name:latest  # New image version
        ports:
        - containerPort: 80
```

### Step 2: Update the Deployment

After saving the YAML file, apply the update using the following command:

```bash
kubectl apply -f your-app-deployment.yaml
```

Kubernetes will create new Pods and gradually remove the old ones.

## 2. Using the `kubectl set image` Command

Alternatively, you can directly update the image from the command line:

```bash
kubectl set image deployment/your-app-deployment your-app-container=your-username/your-app-name:latest
```

This command updates the image of the container within the specified Deployment.

## 3. Deleting and Recreating the Pod

If you are not using a Deployment and are working with a single Pod, you can delete the existing Pod and create a new one:

### Step 1: Delete the Existing Pod

```bash
kubectl delete pod your-old-pod
```

### Step 2: Create the New Pod

Create the manifest file (YAML) for the new Pod and apply it using the following command:

```bash
kubectl apply -f your-new-pod.yaml
```

## Conclusion

Using a Deployment is generally the best practice for replacing an old Pod with a new one, as it allows for a more stable update process. If you are not using a Deployment, it is also possible to delete the Pod and create a new one. In either case, you can update your Pods and ensure they continue running smoothly.