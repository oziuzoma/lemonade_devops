import os
import time
import requests
from prometheus_client import start_http_server, Gauge

# Read environment variables
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
RABBITMQ_API_URL = f'http://{RABBITMQ_HOST}:15672/api/queues'

# Prometheus metric definitions
queue_messages = Gauge('rabbitmq_individual_queue_messages', 'Total messages in the queue', ['host', 'vhost', 'name'])
queue_messages_ready = Gauge('rabbitmq_individual_queue_messages_ready', 'Ready messages in the queue', ['host', 'vhost', 'name'])
queue_messages_unacknowledged = Gauge('rabbitmq_individual_queue_messages_unacknowledged', 'Unacknowledged messages in the queue', ['host', 'vhost', 'name'])

def fetch_queue_metrics():
    """Fetch queue metrics from RabbitMQ API and update Prometheus metrics."""
    try:
        # Make the request to the RabbitMQ API
        response = requests.get(RABBITMQ_API_URL, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
        response.raise_for_status()  # Raise error for invalid HTTP responses

        # Parse the JSON response
        queues = response.json()

        # Iterate over each queue and update Prometheus metrics
        for queue in queues:
            vhost = queue['vhost']
            name = queue['name']
            messages = queue.get('messages', 0)
            messages_ready = queue.get('messages_ready', 0)
            messages_unacknowledged = queue.get('messages_unacknowledged', 0)

            # Set the values for the defined metrics
            queue_messages.labels(host=RABBITMQ_HOST, vhost=vhost, name=name).set(messages)
            queue_messages_ready.labels(host=RABBITMQ_HOST, vhost=vhost, name=name).set(messages_ready)
            queue_messages_unacknowledged.labels(host=RABBITMQ_HOST, vhost=vhost, name=name).set(messages_unacknowledged)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from RabbitMQ: {e}")

def run_prometheus_exporter():
    """Start the Prometheus exporter and periodically fetch queue metrics."""
    start_http_server(8000)  # Start Prometheus metrics server on port 8000
    print("Prometheus exporter started on port 8000")

    while True:
        fetch_queue_metrics()
        time.sleep(10)  # Sleep for 10 seconds before fetching the metrics again

if __name__ == '__main__':
    run_prometheus_exporter()