In Kubernetes, deployments are used to manage the deployment of applications, ensuring that the desired number of replicas of a pod are running at all times. Below is a list of common `kubectl` commands related to deployments, along with brief descriptions:

### Common `kubectl` Commands for Deployments

1. **List Deployments**
   ```bash
   kubectl get deployments
   ```
   - Lists all deployments in the current namespace.

2. **Describe a Deployment**
   ```bash
   kubectl describe deployment <deployment-name>
   ```
   - Provides detailed information about a specific deployment, including its strategy, replicas, and events.

3. **Create a Deployment**
   ```bash
   kubectl create deployment <deployment-name> --image=<image>
   ```
   - Creates a new deployment using the specified image.

4. **Update a Deployment**
   ```bash
   kubectl set image deployment/<deployment-name> <container-name>=<new-image>
   ```
   - Updates the image of a specified container within the deployment.

5. **Scale a Deployment**
   ```bash
   kubectl scale deployment <deployment-name> --replicas=<number>
   ```
   - Scales the number of replicas for a deployment.

6. **Rollback a Deployment**
   ```bash
   kubectl rollout undo deployment/<deployment-name>
   ```
   - Rolls back to the previous version of a deployment.

7. **Check Rollout Status**
   ```bash
   kubectl rollout status deployment/<deployment-name>
   ```
   - Checks the status of a deployment rollout.

8. **Get Deployment YAML/JSON**
   ```bash
   kubectl get deployment <deployment-name> -o yaml
   ```
   - Retrieves the deployment configuration in YAML format.

   ```bash
   kubectl get deployment <deployment-name> -o json
   ```
   - Retrieves the deployment configuration in JSON format.

9. **Delete a Deployment**
   ```bash
   kubectl delete deployment <deployment-name>
   ```
   - Deletes a specified deployment.

10. **Edit a Deployment**
    ```bash
    kubectl edit deployment <deployment-name>
    ```
    - Opens the deployment configuration in your default text editor for inline editing.

11. **View Deployment History**
    ```bash
    kubectl rollout history deployment/<deployment-name>
    ```
    - Displays the rollout history of a deployment.

12. **Pause a Deployment**
    ```bash
    kubectl rollout pause deployment/<deployment-name>
    ```
    - Pauses a deployment, preventing further changes.

13. **Resume a Deployment**
    ```bash
    kubectl rollout resume deployment/<deployment-name>
    ```
    - Resumes a paused deployment.

### Example of Deployment Creation

Here's an example of how to create a deployment using a YAML file:

1. **Create a YAML file (e.g., `my-deployment.yaml`)**:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: my-deployment
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: my-app
     template:
       metadata:
         labels:
           app: my-app
       spec:
         containers:
         - name: my-container
           image: my-image:latest
           ports:
           - containerPort: 8080
   ```

2. **Apply the YAML file**:
   ```bash
   kubectl apply -f my-deployment.yaml
   ```

### Summary

These commands provide a comprehensive toolkit for managing deployments in Kubernetes. Depending on your needs, you can create, update, scale, and monitor your applications effectively. If you have any specific questions or need further details on any command, feel free to ask!