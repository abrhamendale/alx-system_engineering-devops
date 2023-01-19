#!/usr/bin/env bash
#Create server using puppet
exec {'sudo apt-get update':}
exec {'sudo apt-get install nginx':}
exec {'sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default':}
exec { 'sudo service nginx restart':}
