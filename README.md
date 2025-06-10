## What is NGINX?

NGINX (or "Engine X") is a powerful web server, proxy server, and load balancer developed by Igor Sysoev in the early 2000s. It excels in performance due to its asynchronous, event-driven architecture.

### Primary Roles

* **Web Server:** When you access a server through a browser, NGINX can directly serve files from its disk. This is perfect for static content like HTML, CSS, JavaScript, and images.

* **Proxy Server:** This is its more powerful role. A proxy is a server that acts as a middleman for requests from clients seeking resources from other servers.

### Core Functionalities

* **Static File Serving:** Efficiently serves files over HTTP/HTTPS directly from disk.

* **Reverse Proxying:** Forwards client requests to backend servers (e.g., Python, Node.js) without exposing the backend to clients.

* **Load Balancing:** Distributes incoming requests across multiple backend servers to ensure balanced workload and reliability.

* **SSL/TLS Termination:** Manages encryption/decryption for HTTPS, relieving backend servers of this computational overhead.

* **HTTP Caching:** Stores server responses in memory or disk cache for faster retrieval of identical requests, reducing load on backend servers.

* **Rate Limiting:** Controls the number of requests clients can make within a specified time to protect against abuse or faulty clients.

### Alternatives

| Tool | Focus | Key Strengths | When to Consider |
| ---- | ---- | ---- | ---- |
| NGINX | Web Server, Proxy, Load Balancer | High performance, low memory usage, feature-rich. | Most modern web applications. |
| Apache HTTP Server | Web Server with extensive module ecosystem | Flexibility, powerful .htaccess files  | Shared hosting or specific modules not available in NGINX.                |
| HAProxy | TCP/HTTP Load Balancer and Proxy | Extreme performance, advanced load-balancing features | Highly specialized load balancing needs. |
| Cloud Load Balancers | Managed Load Balancing as a Service | Automatic scaling, deep integration with cloud services | Deeply integrated cloud environments preferring managed solutions. |
| Envoy Proxy | Modern, Cloud-Native Proxy | Designed for microservices and service meshes, highly extensible | Advanced cloud-native architectures, often managed by systems like Istio. |


## 1. Setting up NGINX [Locally]

We'll cover the installation on two major Linux distribution: Debian/Ubuntu and RHEL and its derivatives like CentOS, Oracle Linux, Rocky Linux, AlmaLinux.

### a. Installation on Ubuntu/Debian:

Before you install NGINX, you need to set up NGINX packages repository. After that, you can install and update NGINX from the repository.

#### **For Ubuntu**:
Install the prerequisites:
```
sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring
```

Import an official nginx signing key so apt could verify the packages authenticity. Fetch the key:
```
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
```

To set up the apt repository for **stable nginx packages**, run the following command:
```
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

If you would like to use **mainline nginx packages**, run the following command instead:
```
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

Set up repository pinning to prefer our packages over distribution-provided ones:
```
echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
```

To install nginx, run the following commands:
```
sudo apt update
sudo apt install nginx
```

#### **For Debian**:
Install the prerequisites:
```
sudo apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring
```

Import an official nginx signing key so apt could verify the packages authenticity. Fetch the key:
```
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
```

Verify that the downloaded file contains the proper key:
```
gpg --dry-run --quiet --no-keyring --import --import-options import-show /usr/share/keyrings/nginx-archive-keyring.gpg
```

To set up the apt repository for stable nginx packages, run the following command:
```
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

If you would like to use mainline nginx packages, run the following command instead:
```
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/mainline/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

Set up repository pinning to prefer our packages over distribution-provided ones:
```
echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
```

To install nginx, run the following commands:
```
sudo apt update
sudo apt install nginx
```

### b. Installation on RHEL and derivatives:
Install the prerequisites:
```
sudo yum install yum-utils
```

To set up the yum repository, create the file named /etc/yum.repos.d/nginx.repo with the following contents:
```
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```

By default, the repository for stable nginx packages is used. If you would like to use mainline nginx packages, run the following command:
```
sudo yum-config-manager --enable nginx-mainline
```

To install nginx, run the following command:
```
sudo yum install nginx
```

When prompted to accept the GPG key, verify that the fingerprint matches ```573B FD6B 3D8F BC64 1079 A6AB ABF5 BD82 7BD9 BF62```, and if so, accept it.

### c. Management Commands

To interact with the NGINX service, you have to know these management commands.

- To start the NGINX service if it's stopped:
``` bash
sudo systemctl start nginx
```

- To stop the NGINX service completely:
```
sudo systemctl stop nginx
```

- To restart the service (a full stop and then a start):
```
sudo systemctl restart nginx
```

- To enable NGINX to automatically start when the server boots up:
```
sudo systemctl enable nginx
```

- To disable NGINX from starting on boot:
```
sudo systemctl disable nginx
```

- To reload the service:
```
sudo systemctl reload nginx
```
---
**NOTE :-** 

- A '**restart**' causes the server to go down for a brief moment as it kills all NGINX processes and starts new ones. 

- While a '**reload**' is far more graceful. It tells the main NGINX process to load the new configuration, then starts new worker processes with that new configuration. It then tells the old workers to finish serving their current requests before they shut down. The result is a seamless configuration update with zero downtime.

## 2. Setting up NGINX [Cloud]

While installing NGINX locally on a VM is great for learning, real-world applications run in the cloud. The process involves two main stages:

1. **Provisioning Infrastructure:** Creating a virtual server and configuring its network.

2. **Installing Software:** Connecting to that server and installing NGINX, just like we did locally.

### a. Set-up on AWS (Amazon Web Services)

On AWS, a virtual server is called an EC2 (Elastic Compute Cloud) Instance.

**Step 1: Launch an EC2 Instance**

- Log in to the AWS Management Console and navigate to the EC2 service.

- Click "Launch instances".

- Choose an AMI (Amazon Machine Image): Select Ubuntu Server 24.04 LTS.

- Choose an Instance Type: Select t2.micro, as it's eligible for the AWS Free Tier.

- Create a Key Pair: This is essential for SSH access. Create a new key pair, give it a name, and download the .pem file. Keep this file secure!

**Step 2: Configure the Security Group**
*   A Security Group acts as a virtual firewall for your instance. During the launch process, create a new security group with the following inbound rules:
    *   **Rule 1 (for SSH):**
        *   **Type:** `SSH`
        *   **Port:** `22`
        *   **Source:** `My IP` (This is more secure as it only allows you to connect).
    *   **Rule 2 (for Web Traffic):**
        *   **Type:** `HTTP`
        *   **Port:** `80`
        *   **Source:** `Anywhere (0.0.0.0/0)`
    *   **Rule 3 (for Secure Web Traffic):**
        *   **Type:** `HTTPS`
        *   **Port:** `443`
        *   **Source:** `Anywhere (0.0.0.0/0)`

**Step 3: Connect to the Instance**
*   Once your instance is running, select it in the EC2 console to find its **Public IPv4 address**.
*   Open your PowerShell terminal on Windows, navigate to where you saved your `.pem` key, and use the following command to connect:
```
chmod 400 your-key-name.pem

ssh -i "your-key-name.pem" ubuntu@<your-ec2-public-ip>
```

**Step 4: Install NGINX**
*   Use the following commands to install NGINX.
```
sudo apt update
sudo apt install nginx
```
You can now access your NGINX welcome page by visiting `http://<your-ec2-public-ip>` in your browser.

### b. Set-up on Azure

On Microsoft Azure, a virtual server is called a **Virtual Machine (VM)**.

**Step 1: Create a Virtual Machine**
*   Log in to the Azure Portal and search for "Virtual machines".
*   Click "Create" -> "Azure virtual machine".
*   **Image:** Select `Ubuntu Server 24.04 LTS`.
*   **Size:** Choose a free-tier eligible size like `B1s`.
*   **Authentication:** Select "SSH public key" and provide your public key.

**Step 2: Configure Network Security Group (NSG)**
*   An NSG is Azure's virtual firewall. During the VM creation process, you'll reach a "Networking" tab.
*   Under "NIC network security group", select "Advanced".
*   Ensure you have inbound rules that **Allow** traffic for:
    *   `SSH` (port 22)
    *   `HTTP` (port 80)
    *   `HTTPS` (port 443)
    *   Azure's wizard often helps you create these default rules.

**Step 3: Connect to the VM**
*   Once the VM is deployed, go to its overview page to find its **Public IP address**.
*   Open your PowerShell terminal and connect using your username and the VM's IP:

```
ssh your-username@<your-azure-vm-public-ip>
```

**Step 4: Install NGINX**

Use the following commands to install NGINX.
```bash
sudo apt update
sudo apt install nginx
```
You can now access the NGINX welcome page at `http://<your-azure-vm-public-ip>`.

### c. Set-up on GCP (Google Cloud Platform)

On GCP, a virtual server is a **VM Instance** within the **Compute Engine** service.

**Step 1: Create a VM Instance**
*   In the Google Cloud Console, navigate to "Compute Engine" -> "VM instances".
*   Click "Create Instance".
*   **Machine type:** Choose `e2-micro` (part of the free tier).
*   **Boot disk:** Click "Change" and select `Ubuntu 24.04 LTS`.
*   **SSH Keys:** You can add your public SSH key in the "Security and access" section.

**Step 2: Configure Firewall Rules**
*   In the "Firewall" section during instance creation, simply check the boxes for:
    *   **Allow HTTP traffic**
    *   **Allow HTTPS traffic**
*   GCP manages firewall rules at the VPC network level, and these checkboxes create the necessary rules for you.


**Step 3: Connect to the Instance**
*   On the VM instances page, you will find the **External IP** for your new instance.
*   Open PowerShell and connect via SSH:

```
ssh -i "path/to/your/private/key" your-username@<your-gcp-vm-external-ip>
```

**Step 4: Install NGINX**
*   Finally, use the following commands to install NGINX.

```
sudo apt update
sudo apt install nginx
```
You can now access the NGINX welcome page at `http://<your-gcp-vm-external-ip>`.

## 3. NGINX Configuration File

Everything NGINX does, from serving a simple html page to managing a web of complex microservices, is controlled by a plain text file or rather a configuration file. To become more proficient in NGINX, it is important to understand the structure of these files.

On Ubuntu, NGINX configuration files live in the `/etc/nginx/` directory. But NGINX uses a very smart system to manage different website configs. Let's break down the important locations.

*   **/etc/nginx/nginx.conf**: This is the main configuration file. It controls the high-level settings, like how many worker processes NGINX should run. We rarely need to edit this file directly.

*   **/etc/nginx/sites-available/**: This is your storage folder. You create and save the configuration file for every single website you manage here. Think of it as a collection of blueprints; each file is a blueprint for a different site, whether it's active or not.

*   **/etc/nginx/sites-enabled/**: This is the "live" folder. NGINX only reads this directory to see which websites it should actually run. To activate a site, you create a shortcut (a symbolic link) from its blueprint in `sites-available` into this folder.

This system helps in quickly turning the website on and off. To disable a site, you just delete its symbolic link from `sites-enabled`. The original configuration file remains safe in `sites-available`, ready to be re-enabled later.

### b. Structure: The "Grammar"

The NGINX configuration has a very simple grammar. It's made up of two things:

1.  **Directives:** These are single-line instructions. They consist of a key and a value, and they always end with a semicolon `;`.
    ```nginx
    # Directive 'worker_processes' with value 'auto'
    worker_processes auto;
    ```

2.  **Blocks (or Contexts):** These are containers for directives and other blocks. They group settings for a specific context. A block is defined by a name followed by curly braces `{}`.
    ```nginx
    # A block named 'http'
    http {
        # This block contains directives inside of it
        include       /etc/nginx/mime.types;
        default_type  application/octet-stream;
    }
    ```
Think of it like nested boxes. You have a big `http` box, and inside it, you can have smaller `server` boxes, and inside those, you have even smaller `location` boxes.

### c. The Core Blocks:

The Block ecosystem follows a hierarchy.

#### The `events` block
This block sits at the top level and deals with connection processing.
```nginx
events {
    worker_connections 768; # How many connections each worker can handle
}
```
For the most part, we can leave this block with its default settings.

#### The `http` block
This is the main container for all of your web-related configurations. Almost everything we do will live inside this block.
```nginx
http {
    # Directives here apply to all websites (server blocks) that we define inside this http block.

    # ... server blocks go here ...
}
```

#### The `server` block

Each `server` block defines a separate virtual server, or website. This is how NGINX can host multiple websites on a single machine.
```nginx
server {
    # This server block "listens" for traffic on port 80 (standard HTTP)
    listen 80;

    # It responds to requests for 'yourdomain.com' or 'www.yourdomain.com'
    server_name yourdomain.com www.yourdomain.com;

    # ... location blocks go here ...
}
```

#### The `location` block
This is arguably the most powerful block. It lives inside a `server` block and lets you decide what to do with a request based on its URL.

```nginx
location / {
    # This block matches ANY request, since all URLs start with "/"
    # It's a great "catch-all"
}

location /images/ {
    # This block will only match requests for URLs that start with /images/, like yourdomain.com/images/logo.png
}

location /api/ {
    # This block will only match requests for your API, like yourdomain.com/api/users
}
```
Inside a `location` block, you use directives to tell NGINX what to do with the matched request—serve a file, pass the request to another server, return an error, etc.
