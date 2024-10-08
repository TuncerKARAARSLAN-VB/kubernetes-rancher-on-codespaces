Here are some basic commands you can use to learn about the Linux operating system and gather information about the system:

### 1. **System Information**
- **Linux Distribution and Version**:
  ```bash
  lsb_release -a
  ```
  This command shows the installed Linux distribution and its version.

- **Kernel Version**:
  ```bash
  uname -r
  ```
  Displays the version of the running Linux kernel.

- **System Information**:
  ```bash
  uname -a
  ```
  Shows general information about the running system (kernel name, version, architecture, etc.).

### 2. **Hardware Information**
- **CPU Information**:
  ```bash
  lscpu
  ```
  Provides information about the CPU.

- **Memory Information**:
  ```bash
  free -h
  ```
  Shows the total and available memory amount.

- **Disk Information**:
  ```bash
  lsblk
  ```
  Displays partitions on disks and disk usage status.

### 3. **File and Directory Management**
- **View Current Directory**:
  ```bash
  pwd
  ```
  Shows the full path of the directory you're in.

- **List Files in Directory**:
  ```bash
  ls -l
  ```
  Lists files in the current directory in detail.

- **Change Directory**:
  ```bash
  cd <directory_name>
  ```

- **Create New Directory**:
  ```bash
  mkdir <directory_name>
  ```

- **Delete File**:
  ```bash
  rm <file_name>
  ```

### 4. **Getting Help and Information**
- **Command Help**:
  ```bash
  man <command_name>
  ```
  Provides detailed information about a specific command (e.g., `man ls`).

- **Command Usage Information**:
  ```bash
  <command_name> --help
  ```
  Gives brief information on how to use the command.

### 5. **System Status**
- **View Running Processes**:
  ```bash
  ps aux
  ```
  Lists all running processes in the system.

- **View System Resource Usage**:
  ```bash
  top
  ```
  Shows real-time CPU and memory usage of the system.

### 6. **Network Information**
- **View Network Interfaces**:
  ```bash
  ip a
  ```
  Shows network interfaces and IP addresses in the system.

- **Connection Test**:
  ```bash
  ping <target_address>
  ```
  Performs a connection test to a specified address (e.g., `ping 8.8.8.8`).

### 7. **Software Management**
- **Install Package** (on Debian-based systems):
  ```bash
  sudo apt install <package_name>
  ```

- **Update Packages**:
  ```bash
  sudo apt update && sudo apt upgrade
  ```

### 8. **Viewing Output Page by Page**
- **View Output Page by Page with `less` or `more`**:
  ```bash
  <command> | less
  ```
  Used to read long outputs more comfortably.

### Conclusion
These commands will help you perform basic operations and gather information about the system while working with the Linux operating system. To learn Linux better, you can try these commands and get more information from the man pages.