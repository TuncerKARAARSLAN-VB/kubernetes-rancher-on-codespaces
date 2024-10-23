`etcd` is a distributed key-value store used by Kubernetes to store all cluster data, including configuration data and state information. While `etcd` commands are typically run in the context of etcd management rather than via `kubectl`, here’s a list of common `etcd` commands and their descriptions for managing etcd directly.

### Common `etcd` Command List

1. **Start etcd**
   ```bash
   etcd
   ```
   - Starts the etcd server. You may need to specify additional flags such as `--data-dir`, `--listen-client-urls`, and `--advertise-client-urls`.

2. **Check etcd health**
   ```bash
   etcdctl endpoint health
   ```
   - Checks the health of the etcd cluster.

3. **List all keys**
   ```bash
   etcdctl get "" --from-key
   ```
   - Retrieves all keys stored in etcd.

4. **Get a specific key**
   ```bash
   etcdctl get <key>
   ```
   - Retrieves the value associated with a specific key.

5. **Set a key-value pair**
   ```bash
   etcdctl put <key> <value>
   ```
   - Stores a key-value pair in etcd.

6. **Delete a key**
   ```bash
   etcdctl del <key>
   ```
   - Deletes a specific key from etcd.

7. **Watch for changes to a key**
   ```bash
   etcdctl watch <key>
   ```
   - Watches for changes to a specific key and outputs changes in real-time.

8. **Get the cluster status**
   ```bash
   etcdctl endpoint status
   ```
   - Displays the status of each etcd member in the cluster.

9. **Snapshot etcd data**
   ```bash
   etcdctl snapshot save <snapshot-file>
   ```
   - Saves a snapshot of the etcd database to a file.

10. **Restore etcd from a snapshot**
    ```bash
    etcdctl snapshot restore <snapshot-file>
    ```
    - Restores the etcd database from a specified snapshot file.

11. **Compact the etcd database**
    ```bash
    etcdctl compact <revision>
    ```
    - Compacts the etcd database to reclaim storage space.

12. **Defragment the etcd database**
    ```bash
    etcdctl defrag
    ```
    - Defragments the etcd database, improving performance and reclaiming storage space.

13. **List members of the etcd cluster**
    ```bash
    etcdctl member list
    ```
    - Lists all members of the etcd cluster along with their status.

### Example of Using `etcdctl`

Here’s an example of how to set and get a key-value pair using `etcdctl`:

1. **Set a key**
   ```bash
   etcdctl put my-key "Hello, etcd!"
   ```

2. **Get the value of the key**
   ```bash
   etcdctl get my-key
   ```

### Important Notes

- **Environment Variables**: Make sure to set the necessary environment variables or flags for authentication and connection settings, such as `ETCDCTL_API`, `ETCDCTL_CACERT`, `ETCDCTL_CERT`, and `ETCDCTL_KEY`.
  
- **Versions**: The `etcdctl` commands might vary slightly between different versions of `etcd`. Always refer to the official etcd documentation for the version you are using.

### Summary

These commands provide a comprehensive toolkit for managing etcd, which is a critical component of Kubernetes for storing configuration and state data. If you have any specific questions or need further details on any command, feel free to ask!