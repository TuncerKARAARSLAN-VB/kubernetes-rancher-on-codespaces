# Kubernetes Keywords List

### 1. **Pod**
- The smallest deployable unit in Kubernetes. It can host one or more containers.

### 2. **Node**
- Each physical or virtual machine in a Kubernetes cluster that represents the environment where Pods run.

### 3. **Kubelet**
- An agent that runs on each node and manages the state of Pods.

### 4. **Service**
- An abstraction layer used to provide network access to Pods.

### 5. **Deployment**
- An object used for managing and scaling Pods.

### 6. **ReplicaSet**
- Ensures that a specified number of Pod replicas are running at all times.

### 7. **Namespace**
- A mechanism for grouping and isolating resources within a cluster.

### 8. **ConfigMap**
- An object used to store application configurations.

### 9. **Secret**
- An object used to securely store sensitive information.

### 10. **Volume**
- Used for sharing data between Pods and providing persistence.

### 11. **Job**
- Used for running one-off tasks.

### 12. **CronJob**
- Used for scheduling recurring tasks at specified intervals.

### 13. **LoadBalancer**
- A type of service that routes external traffic to the appropriate Pods.

### 14. **Ingress**
- A resource for managing external HTTP and HTTPS traffic routing.

### 15. **PersistentVolume (PV)**
- A resource type that provides persistent storage space.

### 16. **PersistentVolumeClaim (PVC)**
- A resource type that allows users to request persistent disk space.

### 17. **StatefulSet**
- Manages stateful applications, ensuring each Pod has a unique identity.

### 18. **DaemonSet**
- Ensures that a specific Pod runs on all or some nodes in the cluster.

### 19. **Horizontal Pod Autoscaler (HPA)**
- Automatically adjusts the number of Pods based on demand.

### 20. **ClusterIP**
- A service type that is accessible only within the cluster.

### 21. **NodePort**
- Opens a specific port on each node to allow external access.

### 22. **etcd**
- A distributed key-value store that holds the state of the Kubernetes cluster.
