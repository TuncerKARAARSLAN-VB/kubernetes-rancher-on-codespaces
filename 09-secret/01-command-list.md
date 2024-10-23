In Kubernetes, Secrets are used to store sensitive information, such as passwords, OAuth tokens, and SSH keys. Secrets are encoded in base64 and can be referenced in Pods to avoid exposing sensitive data in your application code. Here’s a list of common `kubectl` commands related to Secrets, along with their descriptions:

### Common `kubectl` Commands for Secrets

1. **List Secrets**
   ```bash
   kubectl get secrets
   ```
   - Lists all Secrets in the current namespace.

2. **Describe a Secret**
   ```bash
   kubectl describe secret <secret-name>
   ```
   - Provides detailed information about a specific Secret, including its data and metadata.

3. **Create a Secret from Literal Values**
   ```bash
   kubectl create secret generic <secret-name> --from-literal=<key>=<value>
   ```
   - Creates a new Secret with key-value pairs specified as literals.

4. **Create a Secret from a File**
   ```bash
   kubectl create secret generic <secret-name> --from-file=<path/to/file>
   ```
   - Creates a new Secret from the contents of a specified file.

5. **Create a Secret from a Directory**
   ```bash
   kubectl create secret generic <secret-name> --from-file=<path/to/directory>
   ```
   - Creates a new Secret from all files in the specified directory.

6. **Update a Secret**
   ```bash
   kubectl apply -f <secret-definition.yaml>
   ```
   - Updates an existing Secret using a YAML file.

7. **Get Secret YAML/JSON**
   ```bash
   kubectl get secret <secret-name> -o yaml
   ```
   - Retrieves the Secret configuration in YAML format.

   ```bash
   kubectl get secret <secret-name> -o json
   ```
   - Retrieves the Secret configuration in JSON format.

8. **Delete a Secret**
   ```bash
   kubectl delete secret <secret-name>
   ```
   - Deletes a specified Secret.

9. **Edit a Secret**
   ```bash
   kubectl edit secret <secret-name>
   ```
   - Opens the Secret configuration in your default text editor for inline editing.

10. **Decode a Secret**
    ```bash
    kubectl get secret <secret-name> -o jsonpath='{.data.<key>}' | base64 --decode
    ```
    - Retrieves and decodes the value of a specific key in the Secret.

### Example of Secret Creation

Here's an example of how to create a Secret using a YAML file:

1. **Create a YAML file (e.g., `my-secret.yaml`)**:
   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: my-secret
   type: Opaque
   data:
     my-key: bXktcGFzc3dvcmQ=  # base64-encoded value of "my-password"
   ```

2. **Apply the YAML file**:
   ```bash
   kubectl apply -f my-secret.yaml
   ```

### Summary

These commands provide a comprehensive toolkit for managing Secrets in Kubernetes. Using Secrets helps protect sensitive data from being exposed in your application's code or configuration files. If you have any specific questions or need further details on any command, feel free to ask!