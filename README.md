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
```bash
sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring
```

Import an official nginx signing key so apt could verify the packages authenticity. Fetch the key:
```bash
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
```

To set up the apt repository for **stable nginx packages**, run the following command:
```bash
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

If you would like to use **mainline nginx packages**, run the following command instead:
```bash
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

Set up repository pinning to prefer our packages over distribution-provided ones:
```bash
echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
```

To install nginx, run the following commands:
```bash
sudo apt update
sudo apt install nginx
```

#### **For Debian**:
Install the prerequisites:
```bash
sudo apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring
```

Import an official nginx signing key so apt could verify the packages authenticity. Fetch the key:
```bash
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
```

Verify that the downloaded file contains the proper key:
```bash
gpg --dry-run --quiet --no-keyring --import --import-options import-show /usr/share/keyrings/nginx-archive-keyring.gpg
```

To set up the apt repository for stable nginx packages, run the following command:
```bash
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

If you would like to use mainline nginx packages, run the following command instead:
```bash
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/mainline/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
```

Set up repository pinning to prefer our packages over distribution-provided ones:
```bash
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

## 4. Setting up a Reverse Proxy

This is one of the most common and powerful uses for NGINX.

A reverse proxy is the single point of contact that manages access to every backend server. Client connects to NGINX, and NGINX—based on your rules—forwards the request to the correct backend application.

**Why is this so useful?**
*   **Hides your backend:** Clients don't know the IP address or port of your application, which is great for security.
*   **Single point of control:** You can manage SSL/TLS encryption and logging in one place (NGINX).
*   **Flexibility:** It's the foundation for more advanced setups like load balancing.

### SANDBOX: Proxying to a Simple Web App

Our task is to have NGINX listen for a web traffic and forward it to a simple web application on our server.

#### Step 1: Create a Backend Application

We need an application for NGINX to proxy to. A simple Python Flask app is perfect for this.

First, let's install Flask:
```bash
sudo apt update
sudo apt install python3-flask
```

Next, create a directory for our app and create a simple Python file.
```bash
mkdir my-app && cd my-app

nano app.py
```

Paste the following code into the file:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from the Flask Backend App!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Now, execute the Python script to run the application. We'll use `&` to run it in the background so we can continueusing our terminal.
```bash
python3 app.py &
```
You should see output indicating that the app is running on `http://0.0.0.0:5000`. Our backend is now live!

#### Step 2: Configure NGINX as a Reverse Proxy

Now, we'll create a new NGINX configuration to forward requests to our running Flask app.

We will create a new NGINX config file in `sites-available`.
```bash
sudo nano /etc/nginx/sites-available/my-app
```

Paste the following configuration into the file. The comments explain what each line does.
```nginx
server {
    # This server block will listen on port 80 for all incoming traffic
    listen 80;
    server_name _; # The underscore is a catch-all for any domain name
    
    location / {
        # This is the magic directive. It tells NGINX to forward
        # all requests for this location to our Flask app.
        proxy_pass http://localhost:5000;
}
```

#### Step 3: Enable the Site and Verify

Finally, we enable our new site and apply the changes.

To avoid conflicts, it's good practice to disable the default NGINX welcome page.
```bash
sudo rm /etc/nginx/sites-enabled/default
```

Create the symbolic link to activate our new configuration.
```bash
sudo ln -s /etc/nginx/sites-available/my-app /etc/nginx/sites-enabled/
```

Always test your configuration syntax before reloading the service.
```bash
# Test for syntax errors
sudo nginx -t

# If the test is successful, reload NGINX to apply the changes gracefully
sudo systemctl reload nginx
```

At last, open your web browser and navigate to your VM's IP address: `http://<your_vm_ip>`.

Instead of the NGINX welcome page, you should now see:

**Hello from the Flask Backend App!**

> ### What Just Happened?
>
> 1.  Your browser sent a request to `http://<your_vm_ip>` (which goes to port 80).
> 2.  NGINX received the request on port 80.
> 3.  The `server` block listened on port 80 and matched the request.
> 4.  The `location /` block matched the request's path.
> 5.  The `proxy_pass` directive told NGINX to forward the entire request to the Flask app running on `http://localhost:5000`.
> 6.  The Flask app processed the request and sent back the "Hello..." HTML response.
> 7.  NGINX received this response from Flask and forwarded it back to your browser.


## 5. Setting up Load Balancing

NGINX can act as an incredibly efficient load balancer, playing the role of a "traffic director" for your backend services.

**Why is this essential?**
*   **Scalability:** You can handle more traffic by simply adding more backend servers to the pool.
*   **High Availability:** If one of your backend servers crashes or needs maintenance, NGINX will automatically stop sending traffic to it and route all requests to the healthy servers. This prevents downtime for your users.

### SANDBOX: Distribute Traffic Between Two Backend Instances

Our goal is to run two identical instances of our Flask application on different ports and configure NGINX to balance the incoming requests between them.

#### Step 1: Prepare the Backend Applications

To visibly see the load balancer in action, we need to slightly modify our app so we can tell which instance is serving the request.

If your previous Flask app is still running, find its process ID and stop it.
```bash
# Find the process running on port 5000
sudo lsof -i :5000

# Stop it using its PID (Process ID)
kill <PID_from_previous_command>
```

Let's edit our `app.py` file to include a server identifier.
```bash
cd ~/my-app
nano app.py
```

Update the code to look like this. We'll use an environment variable to tell each instance who it is.
```python
from flask import Flask
import os
app = Flask(__name__)

# Get a server ID from an environment variable, defaulting to "Unknown"
server_id = os.environ.get('SERVER_ID', 'Unknown')
@app.route('/')
def home():
    return f"<h1>Response from Backend Server: {server_id}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

*Note: We are still having the app listen on port 5000 in the code, but we will override this from the command line.*

Now, we'll launch two separate processes from the command line, assigning each a unique `SERVER_ID` and running them on different ports (`5001` and `5002`).
```bash
# Launch Server 1 on port 5001
SERVER_ID="Alpha" python3 -m flask run --host=0.0.0.0 --port=5001 &

# Launch Server 2 on port 5002
SERVER_ID="Bravo" python3 -m flask run --host=0.0.0.0 --port=5002 &
```
We now have two backend servers ready to receive traffic.

#### Step 2: Configure NGINX for Load Balancing

Now we introduce a new NGINX block: `upstream`. The `upstream` block defines a named pool of servers that NGINX can send traffic to.

Open the `reverse-proxy` configuration file we created in the last section.
```bash
sudo nano /etc/nginx/sites-available/my-app
```

Modify the file to include the `upstream` block and change the `proxy_pass` directive.
```nginx
# Define a pool of backend servers. We can name this whatever we want.
upstream backend_servers {
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
}

server {
    listen 80;
    server_name _;

    location / {
        # Change proxy_pass to point to our named upstream block.
        # NGINX will now distribute requests between the servers in that block.
        proxy_pass http://backend_servers;
    }
}
```

#### Step 3: Test and Reload

As always, test the configuration syntax before applying it.

```bash
# Test for syntax errors
sudo nginx -t

# If the test is successful, reload NGINX
sudo systemctl reload nginx
```


At last, open your web browser and navigate to your VM's IP address: `http://<your_vm_ip>`.

You will see one of the following responses:

**Response from Backend Server: Alpha**

Now, **refresh your browser several times**. You will see the response change to:

**Response from Backend Server: Bravo**

> ### What Just Happened?
> By default, NGINX uses a **Round Robin** algorithm.
> 1.  The first request comes into NGINX. NGINX forwards it to the first server in the `upstream` block (`127.0.0.1:5001`).
> 2.  The second request comes in. NGINX forwards it to the second server (`127.0.0.1:5002`).
> 3.  The third request goes back to the first server, and so on.
> #### Pro Tip: Other Load Balancing Methods
> NGINX supports other algorithms. You can specify them in the `upstream` block.
> *   `least_conn`: Sends the next request to the server with the fewest active connections.
> *   `ip_hash`: Ensures that requests from the same client IP address will always be sent to the same server. This is useful for applications that require "sticky sessions".
> ```nginx
> upstream backend_servers {
>     ip_hash;
>     server 127.0.0.1:5001;
>     server 127.0.0.1:5002;
> }
> ```

## 7. Setting up an Encrypted SSL Server (HTTPS)

So far, all the traffic between our users and our NGINX server has been sent in plain text. This is a major security risk. Anyone positioned between the client and the server (e.g., on the same Wi-Fi network) could intercept and read the data.

To solve this, we use **HTTPS (HTTP Secure)**, which encrypts the traffic using an **SSL/TLS certificate**.

HTTPS provides three key security benefits:
1.  **Encryption:** Protects the data from being read by attackers.
2.  **Authentication:** Verifies that you are talking to the correct server and not an impostor.
3.  **Integrity:** Ensures that the data has not been tampered with during transit.

### About SSL/TLS Certificates

To enable HTTPS, your server needs a certificate. There are two main types:

*   **CA-Signed Certificate:** Issued by a trusted Certificate Authority (CA) like **Let's Encrypt**. This is the standard for all production websites. It tells browsers that your server's identity has been verified by a trusted third party.
*   **Self-Signed Certificate:** A certificate that you create and sign yourself. It provides the same level of encryption as a CA-signed certificate, but browsers will not trust it by default because no third party has verified your identity.

For this lab, since we are working on a local VM without a public domain name, we will create and use a **self-signed certificate**.

### SANDBOX: Enable HTTPS and Redirect All HTTP Traffic

#### Step 1: Generate a Self-Signed Certificate

We will use the `openssl` command-line tool to generate a private key and a public certificate.

This single command will generate both a 2048-bit RSA private key and a certificate validfor 365 days.
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
```

You will be prompted to enter information for the certificate (Country Name, State, etc.). Since this is for a local test, you can just press `Enter` to accept the defaults for eachfield.

**Let's break down that command:**
*   `openssl req -x509`: A command for creating X.509 certificates.
*   `-nodes`: "No DES," meaning don't encrypt the private key with a passphrase.
*   `-days 365`: Sets the certificate's validity period.
*   `-newkey rsa:2048`: Creates a new private key using 2048-bit RSA encryption.
*   `-keyout`: Specifies the output path for the private key.
*   `-out`: Specifies the output path for the public certificate.

#### Step 2: Configure NGINX for SSL/TLS

Now we'll tell NGINX to use our newly created key and certificate.

Open the same configuration file we've been using.
```bash
sudo nano /etc/nginx/sites-available/my-app
```

Replace the entire contents of the file with the following. This new configuration creates two `server` blocks: one for the redirect and one to handle the secure traffic.

```nginx
upstream backend_servers {
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
}

# Server block for redirecting HTTP to HTTPS
server {
    listen 80;
    server_name _;

    # This directive sends a 301 Permanent Redirect to the browser,
    # telling it to go to the https version of the requested URL.
    return 301 https://$host$request_uri;
}

# The main server block, now configured for SSL
server {
    # Listen on port 443 and enable SSL/TLS
    listen 443 ssl;
    server_name _;

    # Tell NGINX where to find our certificate and private key
    ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
    ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;

    location / {
        proxy_pass http://backend_servers;
    }
}
```

#### Step 3: Test and Reload

Final check before we go live with our secure configuration.

```bash
# Test for syntax errors
sudo nginx -t

# If successful, reload NGINX
sudo systemctl reload nginx
```

1.  **Navigate to the HTTPS site:** Open your browser and go to `https://<your_vm_ip>`.
2.  **The Browser Warning:** You will see a security warning page from your browser saying "Your connection is not private." **This is expected!** The browser is correctly telling you that while the connection is encrypted, the certificate was signed by an unknown entity (you), not a trusted CA.
3.  **Proceed to the Site:** Click "Advanced" and then "Proceed to <your_vm_ip> (unsafe)".
4.  **Verification:** You should now see your load-balanced Flask application, but this time, if you look at the address bar, you will see `https://` and a lock icon (it may have a warning on it, which is normal for self-signed certs).
5.  **Test the Redirect:** Now, try to navigate to the *insecure* version: `http://<your_vm_ip>`. You should be instantly and automatically redirected to the `https://` version.

## Conclusion

Congratulations on completing this guide! You have successfully journeyed from a basic understanding of NGINX to implementing some of its most powerful features in a hands-on lab environment.

By following these steps, you have learned how to:
*   **Install and manage** the NGINX service on a Linux server.
*   Navigate and understand the **modular configuration structure** of NGINX.
*   Configure NGINX as a **Reverse Proxy** to protect and manage a backend application.
*   Implement **Load Balancing** to distribute traffic for scalability and high availability.
*   Secure your server with an **SSL/TLS certificate** to enable HTTPS.


## Connect with Me

I'm a passionate DevOps engineer focused on building efficient, scalable, and secure infrastructure. I enjoy learning new technologies and sharing my knowledge with the community.

> **Aditya Singh**  
> *Aspiring DevOps and Cloud Engineer*

Feel free to connect with me and check out my other projects:

*   [**LinkedIn**](https://www.linkedin.com/in/aditya-singh-bb8200278)
*   [**GitHub**](https://github.com/AdityaJareda)
