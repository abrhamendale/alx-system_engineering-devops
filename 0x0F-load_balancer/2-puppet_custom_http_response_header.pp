#!/usr/bin/env bash
#Create server using puppet
exec { 'http header':
  command  => 'sudo apt-get update;
	sudo apt-get install nginx;
	sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
	sudo service nginx restart',
  provider => shell,
}
