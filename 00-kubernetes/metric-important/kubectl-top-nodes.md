### 1. Metrics Server'ı Yükleyin

Metrics Server'ı yüklemek için aşağıdaki komutları çalıştırabilirsiniz:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### 2. Yüklemenin Doğrulanması

Metrics Server'ın düzgün çalıştığını doğrulamak için şu komutla Pod'ların durumunu kontrol edebilirsiniz:

```bash
kubectl get pods -n kube-system
```

Bu komut, Metrics Server pod'larını listeleyecektir. Pod'ların `Running` durumda olup olmadığını kontrol edin.

### 3. Metrics Server'ın Hata Ayıklaması

Eğer Metrics Server yüklenmiş ama hala çalışmıyorsa, detaylı hata mesajlarına bakmak için Logs'ları inceleyin:

```bash
kubectl logs -n kube-system -l k8s-app=metrics-server
```

Bu adımlar, genellikle `kubectl top nodes` komutunun çalışmamasına neden olan problemleri çözer.

## NEW PROBLEM: 
E1023 08:53:57.405226       1 scraper.go:149] "Failed to scrape node" err="Get \"https://192.168.49.2:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 192.168.49.2 because it doesn't contain any IP SANs" node="minikube"


Eğer yukarıdaki adımları takip ettiyseniz ve `kubectl top nodes` komutu hala çalışmıyorsa, sorunu daha derinlemesine araştırmak için birkaç ek adım deneyebiliriz:

### 1. Metrics Server'ı Manuel Olarak Yeniden Dağıtın
Bazı ortamlarda, Metrics Server düzgün şekilde yapılandırılmamış olabilir. Bu durumda, aşağıdaki adımlarla Metrics Server'ı kaldırıp yeniden dağıtmayı deneyebilirsiniz:

```bash
kubectl delete -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### 2. Node'lar Arasında Doğru Ağ İletişimini Kontrol Edin
Metrics Server, node'lardan veri toplamak için API sunucusuna bağlanmaya ihtiyaç duyar. Ağ ile ilgili bir sorun olup olmadığını kontrol edin. Örneğin:

```bash
kubectl get nodes -o wide
```

Bu komutla node'ların IP adreslerini görebilir ve node'lar arasında erişim olup olmadığını kontrol edebilirsiniz.

### 3. Cluster API Sunucusuna Erişimin Sağlanıp Sağlanmadığını Kontrol Edin
Metrics Server'ın, API sunucusuna bağlanabildiğinden emin olun. Bunun için Metrics Server pod'larının log'larını inceleyin ve API sunucusuna erişim sorunları olup olmadığını kontrol edin:

```bash
kubectl logs -n kube-system -l k8s-app=metrics-server
```

Bu log'larda herhangi bir hata ya da API sunucusuna erişimle ilgili sorun varsa, güvenlik yapılandırmalarınızı (örneğin, RBAC) kontrol etmelisiniz.

### 4. SSL Sertifikası ve DNS Sorunlarını Kontrol Edin
Bazı durumlarda, Metrics Server HTTPS sertifikaları veya DNS ile ilgili sorunlar yaşayabilir. Bu durumda şu hatalara bakın:

- "x509: certificate signed by unknown authority"
- "no such host"

Bu hatalar varsa, Metrics Server'ın yapılandırma dosyasında `--kubelet-insecure-tls` bayrağını kullanarak kubelet ile güvenli olmayan iletişime izin vermeyi deneyebilirsiniz. Bunun için, `components.yaml` dosyasını düzenleyin ve Metrics Server deployment'ına bu bayrağı ekleyin:

```yaml
spec:
  containers:
  - args:
    - --kubelet-insecure-tls
```

### 5. Kubernetes Cluster'ınızın API Resources'larını Kontrol Edin
Metrics Server düzgün kurulmuşsa ve yine de çalışmıyorsa, API kaynaklarının mevcut olup olmadığını kontrol edin:

```bash
kubectl get apiservices
```

Burada, `v1beta1.metrics.k8s.io` servisi `True` durumda olmalı. Eğer `False` veya eksikse, Metrics API düzgün kurulmamış olabilir.

## PROBLEM CONTINUE

Mevcut YAML dosyanızda zaten `--kubelet-insecure-tls` bayrağını eklemişsiniz, ancak bu sorunun çözülmediğini gösteriyor. Adımları kontrol edelim ve hatayı çözmek için tam yapılandırmayı gözden geçirelim:

### 1. YAML Dosyasını Kontrol Edin
YAML dosyanızın doğru olduğundan emin olun. İşte tam YAML dosyanızın olması gereken hali, `--kubelet-insecure-tls` bayrağını `containers` altında doğru bir yere ekleyerek:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: metrics-server
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: metrics-server
  template:
    metadata:
      labels:
        k8s-app: metrics-server
    spec:
      containers:
      - name: metrics-server
        image: k8s.gcr.io/metrics-server/metrics-server:v0.6.2
        args:
        - --kubelet-insecure-tls  # TLS doğrulamasını devre dışı bırak
        ports:
        - containerPort: 443
          protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: metrics-server
  namespace: kube-system
spec:
  ports:
  - port: 443
    targetPort: 443
  selector:
    k8s-app: metrics-server
```

### 2. YAML'ı Tekrar Uygulayın

Metrics Server'ı bu dosya ile yeniden dağıtın:

```bash
kubectl apply -f components.yaml
```

### 3. Hata Ayıklama için Logları İnceleyin

Eğer sorun hala devam ediyorsa, Metrics Server'ın loglarını tekrar kontrol edin:

```bash
kubectl logs -n kube-system -l k8s-app=metrics-server
```

### 4. Node'ların Kubelet Ayarlarını Kontrol Edin

Eğer sorun çözülmezse, kubelet sertifika doğrulamasıyla ilgili ek ayarlara ihtiyacınız olabilir. `kubelet`'in TLS sertifikalarının doğrulanmasını bypass eden ayarlarla çalıştığından emin olun.

```bash
kubectl describe nodes
```

Node'larınızın ayarlarını kontrol ederek, özellikle kubelet'in doğru ayarlarla çalıştığından emin olun.

Bu adımlarla TLS hatasını çözebilir ve `metrics-server`ın düzgün çalışmasını sağlayabilirsiniz.
