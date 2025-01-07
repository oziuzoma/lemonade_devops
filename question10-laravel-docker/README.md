# Laravel Docker Setup

This repository contains a `Dockerfile` to easily containerize your Laravel application with PHP-FPM. The setup installs necessary dependencies, runs Composer to install Laravel's dependencies, and exposes the PHP-FPM server on port 9000.

## Prerequisites

- Docker installed on your machine.
- A Laravel application ready to be containerized.

## Dockerfile Overview

- **PHP-FPM**: Uses the official `php:8.1-fpm` image.
- **Dependencies**: Installs necessary libraries for Laravel (e.g., `gd`, `pdo_mysql`).
- **Composer**: Installs Composer for managing PHP dependencies.
- **Ports**: Exposes port `9000` for PHP-FPM to handle requests.

## Getting Started

### 1. Clone this repository (if you haven't already)

```bash
git clone https://github.com/oziuzoma/lemonade_devops.git
cd question10-laravel-docker

Build the Docker Image

```bash
docker build -t laravel-app .

Run the Docker Container
To run the container and expose it on port 9000:

```bash
docker run -p 9000:9000 -v $(pwd):/var/www laravel-app

Start the container with PHP-FPM running on port 9000.
Mount your current directory ($(pwd)) into the container at /var/www.

Access Your Application
Your Laravel application should now be running inside the container. You can access it via http://localhost:9000.

Install Laravel Dependencies
If you haven't already, run composer install inside the container to install the Laravel application's dependencies:

```bash
Copy code
docker exec -it <container_id> bash
composer install --no-dev --optimize-autoloader