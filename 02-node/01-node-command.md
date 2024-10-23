Here’s a comprehensive list of commonly used `kubectl` commands related to managing nodes in a Kubernetes cluster:

### Basic Node Commands

1. **List all nodes:**
   ```bash
   kubectl get nodes
   ```

2. **Describe a specific node:**
   ```bash
   kubectl describe node <node-name>
   ```

3. **Get node details in YAML format:**
   ```bash
   kubectl get nodes -o yaml
   ```

4. **Get node details in JSON format:**
   ```bash
   kubectl get nodes -o json
   ```

### Node Management Commands

5. **Drain a node (mark it as unschedulable):**
   ```bash
   kubectl drain <node-name> --ignore-daemonsets
   ```

6. **Uncordon a node (mark it as schedulable again):**
   ```bash
   kubectl uncordon <node-name>
   ```

7. **Delete a node from the cluster:**
   ```bash
   kubectl delete node <node-name>
   ```

8. **Label a node:**
   ```bash
   kubectl label nodes <node-name> <label-key>=<label-value>
   ```

9. **Remove a label from a node:**
   ```bash
   kubectl label nodes <node-name> <label-key>-
   ```

### Node Status and Resource Monitoring

10. **Get detailed status of nodes:**
    ```bash
    kubectl get nodes -o wide
    ```

11. **Check resource usage for nodes (requires metrics server):**
    ```bash
    kubectl top nodes
    ```

### Filtering and Sorting

12. **List nodes with specific labels:**
    ```bash
    kubectl get nodes --selector=<label-key>=<label-value>
    ```

13. **Sort nodes by specific fields (e.g., status):**
    ```bash
    kubectl get nodes --sort-by=.status.conditions[?(@.type=="Ready")].status
    ```

### Additional Useful Commands

14. **Get a specific node's labels:**
    ```bash
    kubectl get node <node-name> --show-labels
    ```

15. **Get a node’s conditions:**
    ```bash
    kubectl get node <node-name> -o=jsonpath='{.status.conditions[*].type}'
    ```

16. **View events related to a node:**
    ```bash
    kubectl get events --field-selector involvedObject.kind=Node,involvedObject.name=<node-name>
    ```

### Example Usage

```bash
# List all nodes
kubectl get nodes

# Get details of a specific node
kubectl describe node node-1

# Drain a node for maintenance
kubectl drain node-1 --ignore-daemonsets

# Uncordon a node after maintenance
kubectl uncordon node-1

# Add a label to a node
kubectl label nodes node-1 environment=production

# Get resource usage of nodes
kubectl top nodes
```

### Summary
These commands are essential for managing nodes in a Kubernetes environment. You can always refer to the official Kubernetes documentation for more advanced usage and additional options.