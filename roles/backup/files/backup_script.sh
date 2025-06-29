#!/bin/bash

BACKUP_DIR="/opt/db_backups"
DB_NAME="flaskdb"
DB_USER="flaskuser"
DB_PASS="flaskpass123"
DATE=$(date +%F_%H-%M)
LOG_FILE="/var/log/db_backup.log" # ملف لحفظ سجل الأخطاء

mkdir -p $BACKUP_DIR 2>>$LOG_FILE

mysqldump -u $DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/${DB_NAME}_$DATE.sql 2>>$LOG_FILE

if [ $? -ne 0 ]; then
    echo "Backup failed! Check $LOG_FILE for details."
else
    echo "Backup successful: $BACKUP_DIR/${DB_NAME}_$DATE.sql"
fi