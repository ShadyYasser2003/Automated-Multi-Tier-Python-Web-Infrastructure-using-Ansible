#!/bin/bash

if systemctl is-active --quiet mysql; then
  echo "MySQL is running."
else
  echo "MySQL is down!" | mail -s "MySQL DOWN on $(hostname)" root
fi
