In Kubernetes, namespaces are a way to organize and manage resources in a cluster. They provide a mechanism for isolating groups of resources and can be particularly useful in multi-tenant environments. Here’s a list of common `kubectl` commands related to namespaces, along with their descriptions:

### Common `kubectl` Commands for Namespaces

1. **List Namespaces**
   ```bash
   kubectl get namespaces
   ```
   - Lists all namespaces in the cluster.

2. **Describe a Namespace**
   ```bash
   kubectl describe namespace <namespace-name>
   ```
   - Provides detailed information about a specific namespace.

3. **Create a Namespace**
   ```bash
   kubectl create namespace <namespace-name>
   ```
   - Creates a new namespace.

4. **Delete a Namespace**
   ```bash
   kubectl delete namespace <namespace-name>
   ```
   - Deletes a specified namespace and all resources within it.

5. **Get Resources in a Specific Namespace**
   ```bash
   kubectl get all -n <namespace-name>
   ```
   - Lists all resources (pods, services, deployments, etc.) in the specified namespace.

6. **Set the Default Namespace for kubectl**
   ```bash
   kubectl config set-context --current --namespace=<namespace-name>
   ```
   - Sets the default namespace for the current context, so you don't have to specify `-n <namespace-name>` with each command.

7. **Get Pods in a Specific Namespace**
   ```bash
   kubectl get pods -n <namespace-name>
   ```
   - Lists all pods in the specified namespace.

8. **Get Services in a Specific Namespace**
   ```bash
   kubectl get services -n <namespace-name>
   ```
   - Lists all services in the specified namespace.

9. **Get Deployments in a Specific Namespace**
   ```bash
   kubectl get deployments -n <namespace-name>
   ```
   - Lists all deployments in the specified namespace.

10. **Get ReplicaSets in a Specific Namespace**
    ```bash
    kubectl get replicasets -n <namespace-name>
    ```
    - Lists all ReplicaSets in the specified namespace.

11. **Get Events in a Specific Namespace**
    ```bash
    kubectl get events -n <namespace-name>
    ```
    - Lists all events in the specified namespace.

### Example of Namespace Creation

Here's an example of how to create a namespace using a YAML file:

1. **Create a YAML file (e.g., `my-namespace.yaml`)**:
   ```yaml
   apiVersion: v1
   kind: Namespace
   metadata:
     name: my-namespace
   ```

2. **Apply the YAML file**:
   ```bash
   kubectl apply -f my-namespace.yaml
   ```

### Summary

These commands provide a comprehensive toolkit for managing namespaces in Kubernetes. They help you organize and isolate resources effectively within your cluster. If you have any specific questions or need further details on any command, feel free to ask!