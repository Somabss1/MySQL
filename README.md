# MySQL

This Repository is for my personal learning purposes, The artifacts in this site are  not proprietary and feel free to reuse these scripts. 

#Background
A foreign key (FK) establishes a relationship, or constraint, between two tables which helps to ensure data integrity. It’s very common that Database Foreign Key (FK) issues caused application errors. This manual describes steps to run the Foreign Key check for a MySql database schema and necessary prerequisites.

#Install Python and Mysql Connector for Python

Necessary Python rpms are installed as part of the standard Linux Build,  Please verify and make sure all the Python rpms are installed in the server environment where this tool needs to run. 
Download and Install the appropriate version of MySql Connector for Python in the server.

Run FK Checking Script

Both the script file db_fk_check.py and config.ini should be downloaded to the same directory. 
Run below command to execute the FK check and find output in the corresponding output file

 ./db_fk_check.py > output.txt
