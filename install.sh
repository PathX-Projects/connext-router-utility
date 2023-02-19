#!/usr/bin/env bash
# ROUTER_VERSION="sha-36344e2"

clear

# Confirm that user wants to run script:
echo -e "This utility script will install the Connext Router.\nDeveloped by PathX AI LLC.\n"

read -r -p "Are you sure you want to install and configure the Connext Router? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
    cd ~

    # Installing package dependencies
    echo "Installing package dependencies..."
    
    sudo apt-get install -y ca-certificates curl gnupg lsb-release
    sudo apt-get install -y git docker docker-compose

    # Install the Connext Router
    echo "Installing the Connext Router..."

    cd ~
    git clone https://github.com/connext/router-docker-compose.git

    echo -e "Connext router has been installed!\nInstalling the Connext Router Configuration Utility..."
    
    cd ~
    git clone https://github.com/PathX-Projects/connext-router-utility.git
    
    cd ~/connext-router-utility

    python3 -m utility
else
    exit
fi