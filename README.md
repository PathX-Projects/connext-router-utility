<p float="left">
  <img height=200 src="https://i.ibb.co/yf9cqPx/Path-X-connext.png">
 </p>

# connext-router-utility

This repository contains a CLI utility to accelerate deployment of a Connext router. Intended to be used in conjunction with the PathX AWS Connext Quickstart on Medium:

https://medium.com/@hschick/connext-router-aws-quickstart-guide-252867bc58fe

## Usage

This utility assumes that you have cloned the repository in the same parent directory as the Connext router. For example:

```
parent
├── router-docker-compose
└── connext-router-utility
``` 

Clone the repository, CD into it, and run the install script from the repository root dir:

```bash
git clone https://github.com/PathX-Projects/connext-router-utility.git

cd /connext-router-utility

bash install.sh
```
