#!/bin/sh
cd /nfs/enttoolsdb
/usr/bin/mysqldump --defaults-extra-file=/etc/mysql-backup.cnf --master-data=2 --single-transaction --opt jira9db | /bin/gzip > jira9db_$(date +"%Y%m%d_%H%M%S").sql.gz
/usr/bin/mysqldump --defaults-extra-file=/etc/mysql-backup.cnf --master-data=2 --single-transaction --opt confluence | /bin/gzip > confluence_$(date +"%Y%m%d_%H%M%S").sql.gz
#find /nfs/enttoolsdb -mtime +60 -type f -exec rm -v {} \;
