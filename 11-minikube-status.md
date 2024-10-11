# How to check minikube status and minikube environment

To check the environment where Minikube is running and find out which driver (e.g., Docker, VirtualBox, Hyper-V) it is using, you can use the following commands:

## 1. **Minikube Status Command:**

To view the environment in which Minikube is running, you can use the `minikube status` command. This command shows the status of the cluster and provides information about the driver being used.

```bash
minikube status
```

This command provides general information about the running Minikube cluster and also displays the driver being used.

## 2. **Minikube Profile Info Command:**

To get more detailed information about the cluster, you can use the `minikube profile` command to see the profile details.

```bash
minikube profile
```

This command gives more details about the profile, including the driver in use.

## 3. **Minikube Config View Command:**

To view Minikube’s configuration, you can use the `minikube config view` command. This shows which driver and other configuration settings Minikube is using by default.

```bash
minikube config view
```

## Example Output

If Minikube is running with Docker, the `minikube status` command might produce output like this:

```
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
driver: docker
```

From this output, you can see that Minikube is using the Docker driver, and that the Kubernetes components are running properly.

These commands allow you to easily check the environment where Minikube is running and its driver settings.