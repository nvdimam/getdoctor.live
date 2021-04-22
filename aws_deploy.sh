#!/bin/bash

echo 'Starting to Deploy...'
ssh ec2-user@ec2-3-126-146-213.eu-central-1.compute.amazonaws.com " sudo docker image prune -f 
        cd getdoctor.live 
        docker-compose down
        git fetch origin
        git reset --hard origin/master  &&  echo 'Pulled changes...'
        docker-compose build && APP_ENV=Production docker-compose up -d
        "
echo 'Deployment completed successfully'