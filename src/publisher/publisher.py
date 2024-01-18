import json
import random
import time
import logging
from dapr.clients import DaprClient


def main():
    logging.info("Publisher started")
    time.sleep(1)
    with DaprClient() as dapr_client:
        while True:
            # Generate a random payload
            payload = {"number": random.randint(1, 100)}
            payload_json = json.dumps(payload).encode('utf-8')
            logging.info(f"Publisher publishing random event to uploaded_data topic: {payload}")

            # Publish a message to the topic sorted_data
            dapr_client.publish_event(
                pubsub_name='pubsub',
                topic_name='uploaded_data',
                data=payload_json,
                data_content_type='application/json',
            )
            # Wait for 10 seconds
            time.sleep(1)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    main()
