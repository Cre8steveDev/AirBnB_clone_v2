#!/usr/bin/env bash
# A bash script that sets up a webserver for the deployment
# of web_static directory

# INSTALL NGINX
# Check if the program exists - this will return the full path
command -v nginx &> /dev/null

# Check the previous exit status code to check if it exists
# shellcheck disable=SC2181
if [ $? -ne 0 ]; then 
	sudo apt-get -y update
	sudo apt-get -y install nginx
	sudo ufw allow "Nginx HTTP"
	sudo chown -R "$USER":"$USER" /var/www/html/
	sudo service nginx restart
fi

##############################################
##############################################
# Create Folder Structures if id doesn't alreay exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Check user and group ownership 
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

##############################################
##############################################
# Create fake HTML File 
html_content='<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'

# Copy string content to a file 
echo "$html_content" | sudo  dd status=none of=/data/web_static/releases/test/index.html

##############################################
##############################################
# Create a symbolic link
target_dir="/data/web_static/releases/test/"
link_name="/data/web_static/current"

# Create the symbolic link
sudo ln -s -f "$target_dir" "$link_name"

##############################################
# Target configuration file path (replace with your actual file)
config_file="/etc/nginx/sites-enabled/default"

# Target location block to modify (adjust selector if needed)
target_block="server_name _;"

# Content to insert (replace with your actual domain name)
content="server_name _;\n\ \n\
    location /hbnb_static {\n\
        alias /data/web_static/current/;\n\
        index index.html index.htm;\n\
        autoindex off;\n\
    }\n"

# Search and replace the target block
sudo sed -i "/$target_block/c $content" "$config_file"

# Restart Nginx 
sudo service nginx restart
