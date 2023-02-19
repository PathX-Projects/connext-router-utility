#!/usr/bin/env bash

cd ~/router-docker-compose

# Start the Connext Router
sudo docker-compose create

# Start the Connext router detached
sudo docker-compose up -d

echo -e "\nConnext router has been started!\nYou can check the logs using: sudo docker-compose logs"