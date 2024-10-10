# Merhaba Class - CG Updated This!
Salih
# Installing Minikube in GitHub Codespaces

Minikube allows you to run a local Kubernetes cluster on your machine. Below are the steps to set it up in a GitHub Codespace.

## Prerequisites

Ensure you have the following installed in your Codespace:

1. **Docker**: Minikube uses Docker to create a virtual machine. You can check if Docker is installed by running:
   ```bash
   docker --version
   ```

2. **kubectl**: The command-line tool for managing Kubernetes clusters. Install it using the following command:
   ```bash
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   chmod +x ./kubectl
   sudo mv ./kubectl /usr/local/bin/kubectl
   ```

3. **Minikube**: Install Minikube with the following command:
   ```bash
   curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube
   ```

## Steps to Install Minikube

1. **Update and Upgrade the System**:
   Before proceeding, it's good practice to update the package lists and upgrade installed packages:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Start Minikube with Docker Driver**:
   To start Minikube using Docker as the driver, run the following command:
   ```bash
   minikube start --driver=docker
   ```

3. **Check Minikube Status**:
   Verify that Minikube is running correctly:
   ```bash
   minikube status
   ```

4. **Access the Minikube Dashboard (Optional)**:
   Minikube provides a dashboard for visual management. To launch it, run:
   ```bash
   minikube dashboard
   ```

5. **Using kubectl with Minikube**:
   You can now use `kubectl` to manage your Minikube cluster. For example, check the nodes in your cluster with:
   ```bash
   kubectl get nodes
   ```

## Conclusion

By following these steps, you will have a fully operational Minikube environment in your GitHub Codespace, ready for developing and testing Kubernetes applications.
