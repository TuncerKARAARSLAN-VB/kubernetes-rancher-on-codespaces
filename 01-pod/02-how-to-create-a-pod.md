# How to create pod

To create a Pod in Kubernetes, you typically use a YAML configuration file and then apply it using the `kubectl` command. Here's a step-by-step guide to creating a Kubernetes Pod:

## 1. **Write the Pod YAML Configuration**

First, you need to define the Pod in a YAML file. For example, let's create a file called `my-pod.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-first-pod
  labels:
    app: myapp
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
```

Explanation of the YAML:

- **apiVersion**: Specifies the API version, in this case `v1`.
- **kind**: Defines the type of Kubernetes resource. Here it's a `Pod`.
- **metadata**: Contains the Pod's metadata, including the name and optional labels.
- **spec**: The specification of the Pod. This section defines the containers within the Pod.
  - **containers**: A list of containers to run inside the Pod. Here, we are defining a single container.
  - **name**: Name of the container.
  - **image**: The container image to use (in this case, `nginx`).
  - **ports**: Specifies the port that the container will expose.

## 2. **Apply the YAML Configuration to Create the Pod**

To create the Pod in your Kubernetes cluster, use the following `kubectl` command:

```bash
kubectl apply -f my-pod.yaml
```

This command tells Kubernetes to create a Pod based on the configuration in the `my-pod.yaml` file.

## 3. **Verify the Pod is Running**

After applying the YAML file, you can check the status of your Pod with:

```bash
kubectl get pods
```

You should see output similar to this:

```bash
NAME           READY   STATUS    RESTARTS   AGE
my-first-pod   1/1     Running   0          10s
```

This indicates that the `my-first-pod` is running successfully.

## 4. **Get Detailed Information About the Pod**

To see more detailed information about the Pod, use:

```bash
kubectl describe pod my-first-pod
```

This will give you detailed information about the Pod, including events, configuration details, and the current state.

## 5. **Access the Pod Logs**

If you want to see the logs of the container running inside the Pod:

```bash
kubectl logs my-first-pod
```

This will show the logs output by the container (in this case, `nginx`).

## 6. **Delete the Pod**

If you want to delete the Pod:

```bash
kubectl delete pod my-first-pod
```

This will remove the Pod from your cluster.

## Summary of Commands:

1. Write the Pod YAML configuration in `my-pod.yaml`.
2. Create the Pod:

    ```bash
    kubectl apply -f my-pod.yaml
    ```

3. Check Pod status:

    ```bash
    kubectl get pods
    ```

4. Describe the Pod for detailed info:

    ```bash
    kubectl describe pod my-first-pod
    ```

5. View Pod logs:

    ```bash
    kubectl logs my-first-pod
    ```

6. Delete the Pod:

    ```bash
    kubectl delete pod my-first-pod
    ```

    Delete all pods

    ```bash
    kubectl delete pod --all
    ```

By following these steps, you'll be able to create and manage a Pod in Kubernetes.
