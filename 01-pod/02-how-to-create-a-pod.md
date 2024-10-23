# How to create pod

To create a Pod in Kubernetes, you typically use a YAML configuration file and then apply it using the `kubectl` command. Here's a step-by-step guide to creating a Kubernetes Pod:

## 1. **Write the Pod YAML Configuration**

First, you need to define the Pod in a YAML file. For example, let's create a file called `my-nginx-pod` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-nginx-pod
  labels:
    app: mynginxapp
spec:
  containers:
  - name: my-nginx-container
    image: nginx:latest
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
kubectl apply -f my-nginx-pod.yaml
```

This command tells Kubernetes to create a Pod based on the configuration in the `my-nginx-pod` file.

## 3. **Verify the Pod is Running**

After applying the YAML file, you can check the status of your Pod with:

```bash
kubectl get pods
kubectl get pods -A
```

You should see output similar to this:

```bash
NAME           READY   STATUS    RESTARTS   AGE
my-nginx-pod   1/1     Running   0          10s
```

This indicates that the `my-nginx-pod` is running successfully.

## 4. **Get Detailed Information About the Pod**

To see more detailed information about the Pod, use:

```bash
kubectl describe pod my-nginx-pod
```

This will give you detailed information about the Pod, including events, configuration details, and the current state.

```
Name:             my-nginx-pod
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 22 Oct 2024 15:59:04 +0300
Labels:           app=mynginxapp
Annotations:      <none>
Status:           Running
IP:               10.244.0.4
IPs:
  IP:  10.244.0.4
Containers:
  my-nginx-container:
    Container ID:   docker://f361ee0f0f0cc57d13fcf418f4382da4f0bcf70a607b09b118a832b0a7ccad32
    Image:          nginx:latest
    Image ID:       docker-pullable://nginx@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 22 Oct 2024 15:59:06 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8c6dz (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True
  Initialized                 True
  Ready                       True
  ContainersReady             True
  PodScheduled                True
Volumes:
  kube-api-access-8c6dz:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  3m14s  default-scheduler  Successfully assigned default/my-nginx-pod to minikube
  Normal  Pulling    3m13s  kubelet            Pulling image "nginx:latest"
  Normal  Pulled     3m12s  kubelet            Successfully pulled image "nginx:latest" in 1.482s (1.482s including waiting). Image size: 191670474 bytes.
  Normal  Created    3m12s  kubelet            Created container my-nginx-container
  Normal  Started    3m11s  kubelet            Started container my-nginx-container
```

## 5. **Access the Pod Logs**

If you want to see the logs of the container running inside the Pod:

```bash
kubectl logs my-nginx-pod
```

```
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/10/22 12:59:07 [notice] 1#1: using the "epoll" event method
2024/10/22 12:59:07 [notice] 1#1: nginx/1.27.2
2024/10/22 12:59:07 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2024/10/22 12:59:07 [notice] 1#1: OS: Linux 5.15.153.1-microsoft-standard-WSL2
2024/10/22 12:59:07 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/10/22 12:59:07 [notice] 1#1: start worker processes
2024/10/22 12:59:07 [notice] 1#1: start worker process 29
2024/10/22 12:59:07 [notice] 1#1: start worker process 30
2024/10/22 12:59:07 [notice] 1#1: start worker process 31
2024/10/22 12:59:07 [notice] 1#1: start worker process 32
2024/10/22 12:59:07 [notice] 1#1: start worker process 33
2024/10/22 12:59:07 [notice] 1#1: start worker process 34
2024/10/22 12:59:07 [notice] 1#1: start worker process 35
2024/10/22 12:59:07 [notice] 1#1: start worker process 36
2024/10/22 12:59:07 [notice] 1#1: start worker process 37
2024/10/22 12:59:07 [notice] 1#1: start worker process 38
2024/10/22 12:59:07 [notice] 1#1: start worker process 39
2024/10/22 12:59:07 [notice] 1#1: start worker process 40
2024/10/22 12:59:07 [notice] 1#1: start worker process 41
2024/10/22 12:59:07 [notice] 1#1: start worker process 42
2024/10/22 12:59:07 [notice] 1#1: start worker process 43
2024/10/22 12:59:07 [notice] 1#1: start worker process 44
2024/10/22 12:59:07 [notice] 1#1: start worker process 45
2024/10/22 12:59:07 [notice] 1#1: start worker process 46
2024/10/22 12:59:07 [notice] 1#1: start worker process 47
```

This will show the logs output by the container (in this case, `nginx`).

## 6. **Delete the Pod**

If you want to delete the Pod:

```bash
kubectl delete pod my-nginx-pod
```

This will remove the Pod from your cluster.

## Summary of Commands:

1. Write the Pod YAML configuration in `my-nginx-pod`.
2. Create the Pod:

    ```bash
    kubectl apply -f my-nginx-pod.yaml
    ```

3. Check Pod status:

    ```bash
    kubectl get pods
    ```

4. Describe the Pod for detailed info:

    ```bash
    kubectl describe pod my-nginx-pod
    ```

5. View Pod logs:

    ```bash
    kubectl logs my-nginx-pod
    ```

6. Delete the Pod:

    ```bash
    kubectl delete pod my-nginx-pod
    ```

    Delete all pods

    ```bash
    kubectl delete pod --all
    ```

By following these steps, you'll be able to create and manage a Pod in Kubernetes.

### Some of my yaml works:

[Sample YAML Code - Single Pod Create](./code/my-nginx-pod.yaml)

[Sample YAML Code - Multi Container Pod Create](./code/multi-container-pod.yaml)

[Sample YAML Code - Multi Container With Same Folder Shared Together](./code/multi-container-mounted-same-log.yaml)

[Sample YAML Code - Single Pod Limited Resources](./code/my-pods-limited.yaml)