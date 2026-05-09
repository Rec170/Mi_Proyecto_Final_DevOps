#!/bin/bash

find ~/environment -name "*.log" -type f -mtime +7 -delete

echo "Logs antiguos eliminados."
