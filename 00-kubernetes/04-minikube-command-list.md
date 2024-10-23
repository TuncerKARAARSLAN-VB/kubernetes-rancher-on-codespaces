### Basic Commands

1. **Start Minikube:**
   ```bash
   minikube start
   ```
   Starts a Minikube cluster.

2. **Stop Minikube:**
   ```bash
   minikube stop
   ```
   Stops the Minikube cluster.

3. **Delete Minikube Cluster:**
   ```bash
   minikube delete
   ```
   Deletes the Minikube cluster.

4. **Check Minikube Status:**
   ```bash
   minikube status
   ```
   Displays the status of the Minikube cluster and its components.

5. **Update Minikube:**
   ```bash
   minikube update-check
   ```
   Checks for the latest Minikube version available.

### Configuration and Settings

6. **Configure Minikube:**
   ```bash
   minikube config set <key> <value>
   ```
   Sets a Minikube configuration key.

7. **Get Minikube Configuration:**
   ```bash
   minikube config view
   ```
   Displays the current Minikube configuration.

8. **List Configurations:**
   ```bash
   minikube config view --format=json
   ```
   Shows the configurations in JSON format.

### Cluster Management

9. **SSH into Minikube VM:**
   ```bash
   minikube ssh
   ```
   Opens an SSH session to the Minikube VM.

10. **Dashboard:**
    ```bash
    minikube dashboard
    ```
    Launches the Kubernetes dashboard in a web browser.

11. **Addons:**
    - **List Available Addons:**
      ```bash
      minikube addons list
      ```
      Displays a list of available addons.

    - **Enable an Addon:**
      ```bash
      minikube addons enable <addon-name>
      ```
      Enables the specified addon.

    - **Disable an Addon:**
      ```bash
      minikube addons disable <addon-name>
      ```
      Disables the specified addon.

### Networking

12. **Get Minikube IP Address:**
    ```bash
    minikube ip
    ```
    Displays the IP address of the Minikube cluster.

13. **Expose a Service:**
    ```bash
    kubectl expose deployment <deployment-name> --type=NodePort --name=<service-name>
    ```
    Exposes a deployment as a service.

### Resource Management

14. **Get Cluster Information:**
    ```bash
    kubectl cluster-info
    ```
    Displays information about the cluster.

15. **View Logs:**
    ```bash
    minikube logs
    ```
    Displays logs from the Minikube cluster.

16. **View Resource Usage:**
    ```bash
    kubectl top pods
    ```
    Displays resource usage statistics for pods.

### Kubernetes Integration

17. **Use Minikube Context:**
    ```bash
    kubectl config use-context minikube
    ```
    Switches the current context to the Minikube cluster.

18. **Apply a Kubernetes YAML Configuration:**
    ```bash
    kubectl apply -f <file.yaml>
    ```
    Applies the specified configuration file to the cluster.

### Advanced Features

19. **Start Minikube with Specific Driver:**
    ```bash
    minikube start --driver=<driver-name>
    ```
    Starts Minikube using a specific driver (e.g., `docker`, `virtualbox`).

20. **Enable Ingress Addon:**
    ```bash
    minikube addons enable ingress
    ```
    Enables the NGINX Ingress controller.

### Example Commands

```bash
# Start Minikube cluster
minikube start

# Check Minikube status
minikube status

# Open Minikube dashboard
minikube dashboard

# SSH into Minikube VM
minikube ssh

# Delete Minikube cluster
minikube delete
```
