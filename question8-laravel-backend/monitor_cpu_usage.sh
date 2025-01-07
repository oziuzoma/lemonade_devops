#!/bin/bash

# Define the threshold CPU usage (in percentage)
CPU_THRESHOLD=80

# Define the Laravel backend service name (example: 'laravel-backend')
SERVICE_NAME="laravel-backend"

# Function to check CPU usage
check_cpu_usage() {
    # Get the current CPU usage as a percentage
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo "$CPU_USAGE"
}

# Function to restart the service
restart_service() {
    echo "CPU usage exceeded $CPU_THRESHOLD%. Restarting $SERVICE_NAME..."
    sudo systemctl restart $SERVICE_NAME
}

# Infinite loop to check CPU usage continuously
while true
do
    # Get the current CPU usage
    CURRENT_CPU_USAGE=$(check_cpu_usage)
    
    # Check if the CPU usage exceeds the threshold
    if (( $(echo "$CURRENT_CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
        restart_service
    fi

    # Wait for 1 minute before checking again
    sleep 60
done
