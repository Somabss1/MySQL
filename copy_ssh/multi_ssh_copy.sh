#!/bin/bash

# Set the username and the path to the SSH key on the local machine
username=ssundaram
ssh_key_path=~/.ssh/id_rsa.pub

# Set the list of remote servers
servers=(
    vfx1-cb1data-3.ftscc.net
    vfx1-cb1data-4.ftscc.net
    vfx1-cb1fts-2.ftscc.net
    vfx1-cb1data-2.ftscc.net
    vfx1-cb1index-2.ftscc.net
    vfx1-cb1fts-1.ftscc.net
    vfx1-cb1index-1.ftscc.net
    vfx1-cb1query-2.ftscc.net
    vfx1-cb1query-1.ftscc.net
    vfx1-cb1data-1.ftscc.net
)

# Loop through the servers and copy the SSH key
for server in "${servers[@]}"
do
    echo "Copying SSH key to $server..."
    ssh-copy-id -i $ssh_key_path $username@$server
done