# PROCEDURE:
-------------
•	Installed VMware workstation 17 in Laptop and create a VM with Ubuntu Jammy Jellyfish 22.04 as per the requirement from below documentation.

https://docs.docker.com/desktop/install/linux-install/
 
•	Once VM is deployed, we need to install GNOME for non-GNOME linux environments. But in the ubuntu 22.04 it is installed by default and it can be verified in system details.

Navigation: Settings > About > GNOME version

## Prerequisite:
----------------
* Python
* Docker desktop file
* HTML file
  
## CREATE REPOSITORY FOR DOCKER INSTALLATION:
------------------------------------------
Before we install Docker Engine for the first time on a new host machine, we need to set up the Docker repository.

•	APT- Advanced Package tool is used in the command line to configure repository or install packages in the host.
 
•	The below commands can be used to create repository.
### Add Docker's official GPG key:
* sudo apt-get update
* sudo apt-get install ca-certificates curl
* sudo install -m 0755 -d /etc/apt/keyrings
* sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
* sudo chmod a+r /etc/apt/keyrings/docker.asc
 
### Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
 
### INSTALL THE DOCKER PACKAGE:
--------------------------
If we use a root account to login into the VM, 'sudo' command is not required. Here I am using my account and hence I am delegating Super User authority to my account and sudo commands.

•	Use the below command to install the docker engine in the VM,
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
 
•	If required you can verify the version of docker installed using the below command,
docker --version or docker --v
My environment is installed with the version- "Docker version 27.0.3, build 7d4bcd8"
 
•	Verify if the Docker Engine installation is successful by running below command,
sudo docker run hello-world
 
Note: This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.
 
Reference: https://docs.docker.com/engine/install/ubuntu/

We can use any one of the method to install the docker on ubuntu as mentioned in the below documentation.

(I have used the first method since the VM that I have deployed in the VMware workstation is enabled with the internet connection and able to reach http://download.docker.com to pull the required packages for Docker installation)
 
## WEBAPP FUNCTIONALITY:
----------------------
Webapp functionality is to send a request to the webserver and get the response as an image while loading from the web browser.
 
Creating an application code in python and HTML.
Python will be used as the backend and HTML will act as the front end here.
Python using FLASK is going to act as the webserver here and when we send request to it we are going to get response as an image file.
 
Test performed on local machine: Windows 11
---------------------------------------------
* Installed Visual code and install python extension.
* Created a app.py file and a index.html file.
* Python Flask is a lightweight Python web framework that makes it easy to build web applications quickly.
 
App.py:
-------
 
from flask import Flask, render_template
import random
 
app = Flask(__name__)
 
images = ["https://w7.pngwing.com/pngs/190/922/png-transparent-kubernetes-docker-devops-lxc-mongodb-github-blue-logo-symmetry-thumbnail.png"]
 
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")
 
Index.html:
---------------
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Image</title>
</head>
<body>
    <h1>Random Image</h1>
    <img src="{{ url }}" alt="Random Image">
</body>
</html>
 
Executed the py file and got the output from the terminal as below,
Output: 
---------
PS D:\PG-IITJ\Trimester-2\Fundementals of cloud computing\Projects and assignment\Webapp deployment on docker> & C:/Users/nares/anaconda3/python.exe "d:/PG-IITJ/Trimester-2/Fundementals of cloud computing/Projects and assignment/Webapp deployment on docker/App.py"
 * Serving Flask app 'App'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.20:5000
 
Using the URL, we are able to retrieve the image file as expected from browse.
 
Note: Since I do not want my PC to have all the files, I am using a VM with docker installed using the initial procedure and deploying the webapp in docker and trying to retrieve the image via webserver locally on the VM. 
 
## DEPLOYING WEBAPP in DOCKER:
----------------------------
1. Docker is deployed in the VM using the steps described initially.
2. Verify the python version and flask version installed in your VM. If not installed, install the flask using below commands,
* Create dir for flask using Command 'mkdir flask-app && cd flask-app'
* Pip3 install flask
* Python3 -m flask --version

3.	We need to tell how the application needs to run, so I have installed Visual code and created a folder with the files below,

• Folder- "Documents\Webapp Deployment in Docker"

•	File- "Dockerfile" to tell the application how it is going to run. Created under the folder created and specified 

**File - "Dockerfile"**

#To lockin with python version
FROM python:3.10.12
#To copy file from local to /app directory
COPY . /app
 
WORKDIR /app
 
RUN pip install -r requirements.txt
 
#run the command 
CMD ["Python", "app.py"]


**File- "app.py"**

from flask import Flask, render_template
import random
 
app = Flask(__name__)
 
images = ["https://w7.pngwing.com/pngs/190/922/png-transparent-kubernetes-docker-devops-lxc-mongodb-github-blue-logo-symmetry-thumbnail.png"]
 
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")


**File- "requirements.txt":**

flask==3.0.3
 
**File- "index.html"**

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Image</title>
</head>
<body>
    <h1>Random Image</h1>
    <img src="{{ url }}" alt="Random Image">
</body>
</html>
 
## BUILD A DOCKER IMAGE:
---------------------

1. Navigate in the terminal to path- "Documents/Webapp Deployment in Docker" and run the below command to build the docker image
* Sudo docker build -t webapp1
 
2. Run the application now using the below command from the container image that we created.
* Sudo docker run webapp1 
  
3. Use the URL in local browse and confirm if it is able to fetch the image as desired.
