#!/usr/bin/env bash
cd ~/router-docker-compose

# Shutdown the router and delete data
sudo docker-compose down -v

# Remove all docker images (necessary for switching router version)
sudo docker image prune -a -f