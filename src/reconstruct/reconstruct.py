from typing import Optional
from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
from dapr.clients import DaprClient
from dapr.clients.grpc._response import TopicEventResponse
import time
import random
import json
import logging

app = App()
logging.info(f"Reconstruct started...")


@app.subscribe(pubsub_name='pubsub', topic='sorted_data')
# Subscription using GRPC
def sorted_data(event: v1.Event) -> Optional[TopicEventResponse]:
    logging.info("Received an event with data: ", event.Data())
    # Process the data
    time.sleep(3)

    with DaprClient() as dapr_client:
        # Publish to reconstructed_data topic
        logging.info(f"Completed reconstruction on data")
        reconstructed_data = random.randbytes(20)
        payload = {"data": reconstructed_data}
        payload_json = json.dumps(payload).encode('utf-8')
        dapr_client.publish_event(pubsub_name='pubsub',
                                  topic_name='reconstructed_data',
                                  data=payload_json,
                                  data_content_type='application/json',
                                  )
        logging.info(f"Completed reconstruction on data. Sending message to reconstructed_data topic with contents: {payload_json}")
    return TopicEventResponse("success")


if __name__ == '__main__':
    
    app.run(50051)
