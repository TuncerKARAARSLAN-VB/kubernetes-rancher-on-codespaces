Docker container IDs are typically 64 characters long, but you can use a shortened version of the ID, as the first 12 characters (or more) are usually sufficient for uniqueness. Here’s how to use a shortened container ID:

### Using Shortened Container IDs

#### Example:
1. **List All Containers:**
   ```bash
   docker ps
   ```

   This command shows the list of running containers. Example output might look like this:

   ```
   CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
   3c5e8827c95f        myapp:latest       "python app.py"     5 minutes ago      Up 5 minutes        0.0.0.0:5000->5000  myapp
   5c8f6a1bdeb3        nginx              "nginx -g 'daemon..."   10 minutes ago    Up 10 minutes       0.0.0.0:80->80      webserver
   ```

2. **Using Shortened Container ID in Commands:**
   You can use the **first 12 characters** (or a sufficient portion) of the container ID to execute commands:

   ```bash
   docker logs 3c5e8827c95f
   ```

   or

   ```bash
   docker stop 3c5e8827c
   ```

### Important Notes:
- The ***first 12 characters of the container ID*** are usually sufficient, but if there are multiple containers with similar IDs, you may need to use a longer portion.
- When using a shortened ID, Docker will automatically complete the ID for you.

### Example Usage of Shortened IDs:
- Checking the container's status:
   ```bash
   docker inspect 3c5e8827c95f
   ```

- Removing a container:
   ```bash
   docker rm 5c8f6a1bdeb3
   ```

This way, you can use shortened Docker container IDs for easier command execution.