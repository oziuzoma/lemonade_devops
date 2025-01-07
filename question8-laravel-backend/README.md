# Laravel CPU Monitor and Service Restarter

This project contains a bash script that monitors the system's CPU usage. If the CPU usage exceeds 80%, the script automatically restarts the specified Laravel backend service. This can be useful for ensuring your application remains responsive even during periods of high CPU load.

## Features
- Monitors CPU usage at regular intervals (set via cron job).
- Restarts the Laravel backend service if CPU usage exceeds the specified threshold.
- Configurable service name and CPU threshold.

## Prerequisites
- Linux-based system (Ubuntu, CentOS, etc.).
- A Laravel backend service running with a systemd service manager (e.g., `laravel-backend`, `php-fpm`).
- `sudo` privileges to restart the service.
- Cron installed on your system (default on most Linux distributions).

## Setup Instructions

### 1. Clone the repository (optional)
If you are using Git, you can clone the repository to your local machine.

```bash
git clone https://github.com/oziuzoma/lemonade_devops.git
cd question8-laravel-backend

Make the script executable
Run the following command to make the script executable:

```bash
chmod +x monitor_cpu.sh

Set up a Cron Job
To run the script at regular intervals 30mins, you need to set up a cron job.

```bash
crontab -e

Add the following line to run the script every minute:
```bash
*/30 * * * * /path/to/your/script/monitor_cpu.sh

Replace /path/to/your/script/monitor_cpu.sh with the actual path where you saved the script.

Verify the cron job

```bash
crontab -l
The output should show the entry you added to run the script every minute.