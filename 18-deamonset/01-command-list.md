In Kubernetes, a DaemonSet ensures that a copy of a specific Pod runs on all (or a subset of) nodes in the cluster. This is useful for running background tasks such as log collection, monitoring, or managing storage on each node. Below is a list of common `kubectl` commands related to DaemonSets, along with their descriptions:

### Common `kubectl` Commands for DaemonSets

1. **List DaemonSets**
   ```bash
   kubectl get daemonsets
   ```
   - Lists all DaemonSets in the current namespace.

2. **Describe a DaemonSet**
   ```bash
   kubectl describe daemonset <daemonset-name>
   ```
   - Provides detailed information about a specific DaemonSet, including its Pods, configuration, and events.

3. **Create a DaemonSet from a YAML File**
   ```bash
   kubectl apply -f <daemonset-definition.yaml>
   ```
   - Creates a DaemonSet using the configuration defined in a YAML file.

4. **Delete a DaemonSet**
   ```bash
   kubectl delete daemonset <daemonset-name>
   ```
   - Deletes a specified DaemonSet.

5. **Get DaemonSet YAML/JSON**
   ```bash
   kubectl get daemonset <daemonset-name> -o yaml
   ```
   - Retrieves the DaemonSet configuration in YAML format.

   ```bash
   kubectl get daemonset <daemonset-name> -o json
   ```
   - Retrieves the DaemonSet configuration in JSON format.

6. **Get Pods Managed by a DaemonSet**
   ```bash
   kubectl get pods -l name=<daemonset-name>
   ```
   - Lists all Pods managed by a specific DaemonSet, using labels to filter.

7. **Get Events Related to a DaemonSet**
   ```bash
   kubectl get events --field-selector involvedObject.name=<daemonset-name>
   ```
   - Displays events related to a specific DaemonSet, which can help in troubleshooting issues.

8. **Edit a DaemonSet**
   ```bash
   kubectl edit daemonset <daemonset-name>
   ```
   - Opens the DaemonSet configuration in your default text editor for inline editing.

9. **Rollout a DaemonSet**
   ```bash
   kubectl rollout status daemonset <daemonset-name>
   ```
   - Shows the rollout status of a DaemonSet.

   ```bash
   kubectl rollout history daemonset <daemonset-name>
   ```
   - Displays the rollout history of a DaemonSet.

   ```bash
   kubectl rollout undo daemonset <daemonset-name>
   ```
   - Undoes the last rollout of a DaemonSet.

### Example of DaemonSet Creation

Here’s an example of how to create a DaemonSet using a YAML file:

1. **Create a DaemonSet YAML file (e.g., `my-daemonset.yaml`)**:
   ```yaml
   apiVersion: apps/v1
   kind: DaemonSet
   metadata:
     name: my-daemonset
   spec:
     selector:
       matchLabels:
         name: my-daemonset
     template:
       metadata:
         labels:
           name: my-daemonset
       spec:
         containers:
         - name: my-container
           image: my-image:latest
           ports:
           - containerPort: 80
   ```

2. **Apply the DaemonSet**:
   ```bash
   kubectl apply -f my-daemonset.yaml
   ```

### Summary

These commands provide a comprehensive toolkit for managing DaemonSets in Kubernetes. DaemonSets are essential for ensuring that specific workloads run on every node, making them ideal for services like monitoring, logging, and network services. If you have any specific questions or need further details on any command, feel free to ask!