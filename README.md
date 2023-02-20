<p float="left">
  <img height=200 src="https://i.ibb.co/yf9cqPx/Path-X-connext.png">
 </p>

# connext-router-utility

This repository contains a CLI utility to accelerate deployment of a Connext router. Intended to be used in conjunction with the PathX AWS Connext Quickstart on Medium:

https://medium.com/@hschick/connext-router-aws-quickstart-guide-252867bc58fe

## UNIX Command Line Usage

Update your apt-get dependency manager:

```bash
sudo apt-get update

sudo apt-get install wget
```

Pull the **install.sh** script and install: 

```bash
wget https://raw.githubusercontent.com/PathX-Projects/connext-router-utility/main/scripts/install.sh

bash install.sh
```

This utility creates the following file structure on your machine:

```
~
├── /router-docker-compose  <- Official Connext Router repository 
├── /connext-router-utility  <- This repository
├── install.sh
├── configure.sh
├── start.sh
└── exit.sh
``` 
