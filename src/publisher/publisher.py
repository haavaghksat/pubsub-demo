import json
import random
import asyncio
import logging
from dapr.clients import DaprClient

async def main():
    # Dapr publishes messages using gRPC by default.
    # The default Dapr gRPC port is 50001.
    logging.basicConfig(level = logging.INFO)
    logging.info("Publiser started")

    with DaprClient() as dapr_client:
        while True:
            # Generate a random payload
            payload = {"number": random.randint(1, 100)}
            payload_json = json.dumps(payload).encode('utf-8')
            logging.info(f"Publishing event: {payload}")

            # Publish a message to the topic 'randomNumbers'
            dapr_client.publish_event(
                pubsub_name='pubsub',
                topic_name='randomNumbers',
                data=payload_json,
                data_content_type='application/json',
            ) 
            logging.info('Published data: ', payload)

            # Wait for 2 seconds
            await asyncio.sleep(2)

if __name__ == '__main__':
    asyncio.run(main())
