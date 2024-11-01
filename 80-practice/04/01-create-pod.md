# creating pod service with kubectl

- cd code

- kubectl get pods

- kubectl get svc

- kubens sbm-dev

- kubectl apply -f nginx-pod.yaml

- kubectl get pods

- kubectl apply -f nginx-service.yaml

- kubectl get svc

- kubectl logs nginx-pod

- kubectl port-forward service/nginx-service 8082:80

- html://localhost:8082
