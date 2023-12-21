import json
import random
import asyncio
from dapr.clients import DaprClient

async def main():
    # Dapr publishes messages using gRPC by default.
    # The default Dapr gRPC port is 50001.
    with DaprClient() as dapr_client:
        while True:
            # Generate a random payload
            payload = {"number": random.randint(1, 100)}
            payload_json = json.dumps(payload).encode('utf-8')

            # Publish a message to the topic 'randomNumbers'
            await dapr_client.publish_event(
                pubsub_name='pubsub',
                topic_name='randomNumbers',
                data=payload_json,
                data_content_type='application/json',
            )
            print('Published data: ', payload)

            # Wait for 2 seconds
            await asyncio.sleep(2)

if __name__ == '__main__':
    asyncio.run(main())
