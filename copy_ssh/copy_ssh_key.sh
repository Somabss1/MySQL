#!/bin/bash 
for server in `cat ./list_of_servers`; 
do 
echo "Copying SSH key to $server..."
ssh-copy-id -i ~/.ssh/id_rsa.pub $server

done
