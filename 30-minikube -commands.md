Here's a table of common Minikube commands tailored for use in a Codespace environment. This format can help you quickly reference commands for managing your local Kubernetes cluster with Minikube.

| **Command**                          | **Description**                                             |
|--------------------------------------|-------------------------------------------------------------|
| `minikube start`                    | Initializes and starts a single-node Kubernetes cluster on your local machine using Minikube. This command creates a virtual machine (or uses a container, depending on the driver), installs Kubernetes components, and configures the cluster. It sets up the necessary infrastructure for running Kubernetes locally, including the control plane and worker node components. After execution, you'll have a fully functional Kubernetes environment ready for development and testing purposes. |
| `minikube start --driver=docker`    | Start Minikube with Docker driver.                          |
| `minikube start --memory=4096`      | Start Minikube with specified memory allocation.            |
| `minikube start --cpus=2`           | Start Minikube with specified number of CPUs.               |
| `minikube start --kubernetes-version=v1.20.0` | Start Minikube with a specific Kubernetes version. |
| `minikube stop`                     | Gracefully shuts down the running Minikube cluster. This command halts all running processes within the cluster, including the Kubernetes control plane components and any deployed workloads. It preserves the cluster's state, allowing you to resume operations later without losing your configurations or deployed applications. The command ensures a clean shutdown, preventing potential data corruption or inconsistencies. After execution, the virtual machine or container hosting the Minikube cluster is stopped, freeing up system resources. This is particularly useful when you need to temporarily free up resources on your local machine or when you're finished working with Kubernetes for the day but plan to resume later. |
| `minikube delete`                   | Completely removes the Minikube cluster from your local machine. This command deletes all associated resources, including the virtual machine or container, Kubernetes components, and any deployed workloads. It erases all cluster data, configurations, and persistent volumes. After execution, your system is returned to a state as if Minikube was never installed. This is useful when you want to start fresh, free up resources, or when troubleshooting cluster issues. Note that this action is irreversible, so ensure you've backed up any important data before running this command. |
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
| `minikube config set memory 4096`        | Set the default memory allocation to 4096 MB.          |
| `minikube config set cpus 2`             | Set the default number of CPUs to 2.                   |
| `minikube config set driver docker`      | Set Docker as the default driver.                      |
| `minikube config set kubernetes-version v1.20.0` | Set the default Kubernetes version to v1.20.0. |
| `minikube config set disk-size 20g`      | Set the default disk size to 20 GB.                    |
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
