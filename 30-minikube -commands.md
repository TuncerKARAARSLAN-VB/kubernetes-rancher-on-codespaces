Here's a table of common Minikube commands tailored for use in a Codespace environment. This format can help you quickly reference commands for managing your local Kubernetes cluster with Minikube.

| **Command**                          | **Description**                                             |
|--------------------------------------|-------------------------------------------------------------|
| `minikube start`                    | Start a Minikube cluster.                                   |
| `minikube start --driver=docker`    | Start Minikube with Docker driver.                          |
| `minikube start --memory=4096`      | Start Minikube with specified memory allocation.            |
| `minikube start --cpus=2`           | Start Minikube with specified number of CPUs.               |
| `minikube start --kubernetes-version=v1.20.0` | Start Minikube with a specific Kubernetes version. |
| `minikube stop`                     | Stop the running Minikube cluster.                          |
| `minikube delete`                   | Delete the Minikube cluster.                                |
| `minikube delete --all`             | Delete all Minikube clusters and profiles.                  |
| `minikube status`                   | Check the status of the Minikube cluster, including host, kubelet, apiserver, and kubeconfig. |
| `minikube status -f "{{.Host}}"`      | Get status of the host component only.                      |
| `minikube status -f "{{.Kubelet}}"`   | Check the status of the kubelet component.                  |
| `minikube status -f "{{.APIServer}}"` | Verify the status of the API server component.              |
| `minikube status -f "{{.Kubeconfig}}"` | Check the status of the kubeconfig.                        |
| `minikube status --output json`     | Get detailed status information in JSON format.             |
| `minikube status --output table`    | Display status information in a tabular format.             |
| `minikube dashboard`                | Open the Kubernetes dashboard in your web browser.          |
| `minikube dashboard --url`          | Get the URL of the dashboard without opening the browser.   |
| `minikube config set driver <driver_name>` | Set the driver for Minikube (e.g., `docker`, `virtualbox`). |
| `minikube config view`              | View the current Minikube configuration.                    |
| `minikube config set <property> <value>` | Set a specific configuration property.                 |
| `minikube addons list`              | List all available addons.                                  |
| `minikube addons enable <addon_name>` | Enable a specific Minikube addon (e.g., `ingress`).       |
| `minikube addons disable <addon_name>` | Disable a specific Minikube addon.                       |
| `minikube ssh`                      | SSH into the Minikube VM.                                   |
| `minikube ssh -- <command>`         | Run a command via SSH on the Minikube node.                 |
| `minikube logs`                     | View the logs for the Minikube cluster.                     |
| `minikube logs -f`                  | Follow the logs for the Minikube cluster.                   |
| `minikube ip`                       | Get the IP address of the Minikube cluster.                 |
| `minikube service <service-name>`   | Get the URL of a service in your cluster.                   |
| `minikube service list`             | List the URLs for all services in your cluster.             |
| `minikube tunnel`                   | Create a route to services deployed with type LoadBalancer. |
| `minikube update-check`             | Check for available updates for Minikube.                   |
| `minikube update-context`           | Update the context for kubectl to point to your Minikube cluster. |
| `minikube cache list`               | List all the images currently cached.                       |
| `minikube cache add <image>`        | Add an image to the local cache.                            |
| `minikube cache delete <image>`     | Delete an image from the local cache.                       |
| `minikube mount <source> <target>`  | Mount a directory from the host into the Minikube VM.       |
| `minikube node list`                | List all the nodes in the cluster.                          |
| `minikube node add`                 | Add a node to the cluster.                                  |
| `minikube node delete`              | Delete a node from the cluster.                             |
| `minikube profile list`             | List all Minikube profiles.                                 |
| `minikube profile <name>`           | Set the current Minikube profile.                           |
| `minikube -p minikube docker-env`   | Get the Docker environment variables for Minikube.          |
| `minikube kubectl -- <command>`     | Run a kubectl command against your Minikube cluster.        |


### Usage in Codespace

To use these commands effectively in your Codespace environment, ensure that you have Docker installed and running, as Minikube relies on Docker to create the Kubernetes cluster. Always start with `minikube start` to set up your environment, and use the dashboard for an intuitive way to manage your cluster.
