# RabbitMQ Prometheus Exporter

This is a Python-based Prometheus exporter that connects to a RabbitMQ instance's HTTP API (via the RabbitMQ Management Plugin) and exports metrics about all queues in all vhosts. The exporter tracks the following metrics for each queue:

- `rabbitmq_individual_queue_messages`: Total number of messages in the queue.
- `rabbitmq_individual_queue_messages_ready`: Number of messages that are ready to be consumed.
- `rabbitmq_individual_queue_messages_unacknowledged`: Number of unacknowledged messages in the queue.

## Requirements

- Python 3.x
- Prometheus-compatible monitoring system
- RabbitMQ instance with the Management Plugin enabled

## Setup

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/oziuzoma/lemonade_devops.git
cd question7-rabbitmq-prometheus-exporter

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt

Set environment variables
```bash
export RABBITMQ_HOST="your_rabbitmq_host"
export RABBITMQ_USER="your_username"
export RABBITMQ_PASSWORD="your_password"

Run the exporter

```bash
python rabbitmq_prometheus_exporter.py

Configure Prometheus

To scrape the metrics, add the following job configuration to your Prometheus configuration file (prometheus.yml):

```yaml
scrape_configs:
  - job_name: 'rabbitmq'
    static_configs:
      - targets: ['your_exporter_host:8000']

Then, restart Prometheus to apply the changes.

Once the exporter is running and Prometheus is scraping it, you can view the metrics by visiting http://your_exporter_host:8000/metrics. The metrics will be in the following format:

```bash
# HELP rabbitmq_individual_queue_messages Total messages in the queue
# TYPE rabbitmq_individual_queue_messages gauge
rabbitmq_individual_queue_messages{host="your_rabbitmq_host",vhost="/",name="queue_name"} 100
