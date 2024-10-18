### **What is Ingress Port?**

In Kubernetes, **Ingress Port** refers to the port on which an **Ingress** resource listens for incoming HTTP and HTTPS traffic. An **Ingress** acts as an entry point for external traffic to access services within a Kubernetes cluster. It provides a way to define rules for routing traffic to different services based on the request's host, path, or other attributes.

### **Function of Ingress**

The primary functions of Ingress in Kubernetes include:

1. **Routing Traffic:** Ingress allows you to define rules for routing external HTTP/S traffic to different services within your cluster based on the URL path or hostname. For example, traffic for `example.com/app1` can be routed to one service, while traffic for `example.com/app2` can be routed to another.

2. **Consolidated Entry Point:** Instead of exposing each service with a LoadBalancer or NodePort, Ingress provides a single external IP address through which multiple services can be accessed. This simplifies network management and reduces the need for multiple load balancers.

3. **TLS/SSL Termination:** Ingress can handle TLS/SSL termination, meaning it can manage the secure connection (HTTPS) and forward the decrypted traffic to the backend services. This can simplify certificate management since you only need to manage certificates at the Ingress level rather than at each service.

4. **Advanced Routing Features:** Ingress controllers can offer additional features such as URL rewriting, authentication, and rate limiting, allowing for more complex traffic management scenarios.

### **When is Ingress Used?**

1. **Multiple Services Under One IP:** When you have multiple services that need to be accessed externally, using Ingress allows you to consolidate access under a single IP address or domain name. This is particularly useful in microservices architectures.

2. **Host and Path-based Routing:** If you need to route requests based on the host or URL path, Ingress makes it easy to define these routing rules.

3. **TLS/SSL Management:** Ingress is used when you want to manage SSL/TLS certificates for multiple services efficiently, allowing for HTTPS connections without configuring each service individually.

4. **Simplified Network Management:** Ingress simplifies the management of external access to your services, especially when running applications in a Kubernetes cluster hosted in a cloud environment.

### **How Ingress Works**

Here’s how Ingress operates:

1. **Ingress Resource Definition:** You define an Ingress resource in your Kubernetes YAML configuration file, specifying the rules for routing traffic to various services based on the host and path.

2. **Ingress Controller:** An Ingress controller is responsible for fulfilling the Ingress resource. It is a piece of software (often running as a Pod) that listens to changes in Ingress resources and configures a load balancer or proxy to route incoming traffic accordingly. Popular Ingress controllers include NGINX Ingress Controller, Traefik, and HAProxy Ingress.

3. **Traffic Flow:**
   - When an external request comes in, it hits the Ingress controller.
   - The controller examines the rules defined in the Ingress resource to determine which service to route the traffic to.
   - The controller then forwards the traffic to the appropriate service based on the routing rules.

### **How to Use Ingress in Kubernetes**

To use Ingress, you will typically follow these steps:

1. **Deploy an Ingress Controller:** You need to have an Ingress controller running in your cluster. This can often be done using a Helm chart or Kubernetes manifests. Here's an example of deploying the NGINX Ingress Controller:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
   ```

2. **Create Ingress Resource:** Define an Ingress resource that specifies the routing rules. Here’s an example of an Ingress YAML configuration:

   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: my-ingress
     annotations:
       nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     rules:
       - host: example.com
         http:
           paths:
             - path: /app1
               pathType: Prefix
               backend:
                 service:
                   name: app1-service
                   port:
                     number: 80
             - path: /app2
               pathType: Prefix
               backend:
                 service:
                   name: app2-service
                   port:
                     number: 80
   ```

   In this example:
   - The Ingress resource listens for traffic directed at `example.com`.
   - Traffic for `/app1` is routed to `app1-service`, while traffic for `/app2` is routed to `app2-service`.

3. **Expose the Ingress Controller:** To make the Ingress accessible from the internet, you need to expose the Ingress controller using a service of type `LoadBalancer` or `NodePort`. For example, if using the NGINX Ingress Controller, you can expose it as follows:

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: ingress-nginx
   spec:
     type: LoadBalancer
     ports:
       - port: 80
         targetPort: 80
       - port: 443
         targetPort: 443
     selector:
       app.kubernetes.io/name: ingress-nginx
   ```

4. **Access Your Application:** Once the Ingress resource and the Ingress controller are set up, you can access your applications using the defined host and path. For example, navigating to `http://example.com/app1` would route the request to `app1-service`.

### **Pros of Using Ingress**

1. **Cost-Effective:** By consolidating multiple services under a single IP address, Ingress can reduce costs associated with cloud load balancers.

2. **Flexible Routing:** Ingress allows for advanced routing based on various criteria (host, path), making it suitable for complex microservice architectures.

3. **Centralized SSL Management:** Ingress simplifies the management of SSL/TLS certificates, allowing for easier implementation of secure connections across multiple services.

4. **Improved Traffic Control:** Ingress controllers can provide features such as rate limiting, authentication, and logging, giving more control over incoming traffic.

### **Cons of Using Ingress**

1. **Complexity:** Setting up and managing Ingress controllers can introduce complexity, especially in configuring custom routing rules and handling SSL termination.

2. **Performance Overhead:** Depending on the Ingress controller and configuration, there might be additional latency compared to using a direct service like LoadBalancer or NodePort.

3. **Limited to HTTP/S:** Ingress is primarily designed for HTTP and HTTPS traffic, making it unsuitable for other types of traffic (e.g., TCP/UDP) unless specifically configured through additional controllers.

### **Ingress vs. LoadBalancer vs. NodePort**

- **Ingress:** Provides advanced routing features and handles multiple services under a single external IP. Best suited for web applications with multiple endpoints needing HTTP/S access.
  
- **LoadBalancer:** Automatically provisions a cloud load balancer to expose a service to external traffic. It's simpler for single-service exposure but can become expensive if multiple services require exposure.

- **NodePort:** Exposes a service on a static port on each node. It's useful for development environments but does not provide advanced routing or a consolidated access point for multiple services.

### **Conclusion**

- **What is it?** Ingress Port is the entry point for external HTTP/S traffic to access services within a Kubernetes cluster through defined routing rules in an Ingress resource.

- **When to Use:** Use Ingress when you need to route traffic to multiple services under a single IP address, manage TLS certificates efficiently, or require complex traffic management features.

- **How to Use:** Deploy an Ingress controller, create an Ingress resource defining routing rules, and expose the controller to make your services accessible from the internet.

Ingress is an essential part of Kubernetes networking, enabling sophisticated traffic management and providing a streamlined way to expose multiple services securely and efficiently.