If you've completed all the steps but are unable to deploy your application, it likely indicates that you are facing security issues.


```
kubectl get services
```

| NAME            | TYPE        | CLUSTER-IP       | EXTERNAL-IP   | PORT(S)          | AGE  |
|------------------|-------------|-------------------|---------------|-------------------|------|
| kubernetes      | ClusterIP   | 10.96.0.1        | <none>        | 443/TCP           | 77m  |
| my-python-app    | NodePort    | 10.101.142.171   | <none>        | 8080:31867/TCP    | 34m  |

```
kubectl get pods
```

| NAME                             | READY | STATUS            | RESTARTS | AGE  |
|----------------------------------|-------|-------------------|----------|------|
| my-python-app-59d9f756bc-9jtkh  | 0/1   | ImagePullBackOff  | 0        | 39m  |


# Detailed error log 

```
kubectl describe pod my-python-app-59d9f756bc-9jtkh
```

Name:             my-python-app-59d9f756bc-9jtkh
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 06 Oct 2024 10:35:44 +0000
Labels:           app=my-python-app
                  pod-template-hash=59d9f756bc
Annotations:      <none>
Status:           Pending
IP:               10.244.0.6
IPs:
  IP:           10.244.0.6
Controlled By:  ReplicaSet/my-python-app-59d9f756bc
Containers:
  my-python-app:
    Container ID:   
    Image:          my-python-app
    Image ID:       
    Port:           8080/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-r8w2z (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-r8w2z:
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
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  35m                  default-scheduler  Successfully assigned default/my-python-app-59d9f756bc-9jtkh to minikube
  Normal   Pulling    33m (x4 over 35m)    kubelet            Pulling image "my-python-app"
  Warning  Failed     33m (x4 over 35m)    kubelet            Failed to pull image "my-python-app": Error response from daemon: pull access denied for my-python-app, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
  Warning  Failed     33m (x4 over 35m)    kubelet            Error: ErrImagePull
  Warning  Failed     33m (x6 over 35m)    kubelet            Error: ImagePullBackOff
  Normal   BackOff    29s (x148 over 35m)  kubelet            Back-off pulling image "my-python-app"

  ```
  docker build -t my-python-app .
  ```

  docker build -t my-python-app .
[+] Building 0.8s (10/10) FINISHED                                                                docker:default
 => [internal] load build definition from Dockerfile                                                        0.1s
 => => transferring dockerfile: 197B                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                          0.4s
 => [internal] load .dockerignore                                                                           0.0s
 => => transferring context: 2B                                                                             0.0s
 => [internal] load build context                                                                           0.0s
 => => transferring context: 128B                                                                           0.0s
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:49f94609e5a997dc16086a66ac9664591854031d48e375945a  0.0s
 => CACHED [2/5] WORKDIR /app                                                                               0.0s
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                     0.0s
 => CACHED [4/5] RUN pip install -r requirements.txt                                                        0.0s
 => CACHED [5/5] COPY . .                                                                                   0.0s
 => exporting to image                                                                                      0.0s
 => => exporting layers                                                                                     0.0s
 => => writing image sha256:3b00a367788d4b5aeaafea293ced772eaa2ef422de2d72d15f02f52cf14d8970                0.0s
 => => naming to docker.io/library/my-python-app                                                            0.0s

```
docker build -t my-python-app .
```

When your content is ready, you should package it


```
docker logogg
docker login docker.login
```

It will ask you for your username and password. Go to docker.io in your browser. If you don't have an account, register for a free account and keep your username and password. You will use it in a moment. If you have an account, use your username and password at the login prompt in the docker login command in the terminal screen. 

```
docker tag my-python-app docker.io/tuncerkaraarslan/my-python-app:latest
```

You should publish your package on docker.io.  

```
docker push docker.io/tuncerkaraarslan/my-python-app:latest
```

docker push docker.io/tuncerkaraarslan/my-python-app:latest
The push refers to repository [docker.io/tuncerkaraarslan/my-python-app]
af792a53c530: Pushed 
4b00d368346b: Pushed 
177e5cececc8: Pushed 
68c7d7845763: Pushed 
9e599118e168: Pushed 
e228adf1886f: Pushed 
fb5ccd0db472: Pushed 
8d853c8add5d: Pushed 
latest: digest: sha256:b411e30ac5ad6cf674963e25caa7b01622fd2d63f4f15df04c8e2acf81c44965 size: 1990

![app on docker.io](/images/my-app-image-on-docker-io.png)