Here's a table of common Minikube commands tailored for use in a Codespace environment. This format can help you quickly reference commands for managing your local Kubernetes cluster with Minikube.

| **Command**                          | **Description**                                             |
|--------------------------------------|-------------------------------------------------------------|
| `minikube start`                    | Start a Minikube cluster.                                   |
| `minikube stop`                     | Stop the running Minikube cluster.                          |
| `minikube delete`                   | Delete the Minikube cluster.                                |
| `minikube status`                   | Check the status of the Minikube cluster.                  |
| `minikube dashboard`                 | Open the Kubernetes dashboard in your web browser.         |
| `minikube config set driver <driver_name>` | Set the driver for Minikube (e.g., `docker`, `virtualbox`). |
| `minikube config view`              | View the current Minikube configuration.                    |
| `minikube addons enable <addon_name>` | Enable a specific Minikube addon (e.g., `ingress`).      |
| `minikube addons disable <addon_name>` | Disable a specific Minikube addon.                        |
| `minikube ssh`                      | SSH into the Minikube VM.                                  |
| `minikube logs`                     | View the logs for the Minikube cluster.                    |
| `minikube ip`                       | Get the IP address of the Minikube cluster.                |
| `kubectl <command>` | Execute kubectl commands. (Ensure kubectl is installed).   |
| `kubectl get pods --all-namespaces` | Execute kubectl commands. (Ensure kubectl is installed).  Some exam.  |
| `minikube update-check`             | Check for available updates for Minikube.                  |
| `minikube update-context`           | Update the context for kubectl to point to your Minikube cluster. |

| `minikube -p minikube docker-env` | if you want to know minikube docker environment port. |


### Usage in Codespace

To use these commands effectively in your Codespace environment, ensure that you have Docker installed and running, as Minikube relies on Docker to create the Kubernetes cluster. Always start with `minikube start` to set up your environment, and use the dashboard for an intuitive way to manage your cluster.
