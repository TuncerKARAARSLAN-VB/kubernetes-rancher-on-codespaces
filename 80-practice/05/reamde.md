# publish with deployment 

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sbm-nginx-app
spec:
  replicas: 5  # ReplicaSet 5 olarak ayarlandı
  selector:
    matchLabels:
      app: sbm-nginx-app
  template:
    metadata:
      labels:
        app: sbm-nginx-app
    spec:
      containers:
      - name: sbm-nginx-app
        image: tuncerkaraarslan/sbm-nginx-app:0.3
        ports:
        - containerPort: 80  # Nginx'in default portu

```
