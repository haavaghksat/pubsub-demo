from typing import Optional
from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
from dapr.clients import DaprClient
from dapr.clients.grpc._response import TopicEventResponse
import time
import json
import logging
import numpy as np

app = App()


@app.subscribe(pubsub_name='pubsub', topic='processed_data')
# Subscription using GRPC
def reconstructed_data(event: v1.Event) -> Optional[TopicEventResponse]:
    logging.info(f"Vesseldetector received an event on topic processed_data")
    logging.info(f"Performing vessel detection on data....")
    time.sleep(3)
    n_vessels = np.random.randint(0, 10)
    vessels = [x for x in np.random.rand(n_vessels)]

    logging.info(f"Completed detecting vessels. Found {n_vessels} vessels: {vessels}")
    with DaprClient() as dapr_client:
        # Send message
        payload = {"Vessels": vessels}
        payload_json = json.dumps(payload).encode('utf-8')
        dapr_client.publish_event(pubsub_name='pubsub',
                                  topic_name='detected_vessels',
                                  data=payload_json,
                                  data_content_type='application/json',
                                  )
    logging.info(f"Published message to detected_vessels topic")
    return TopicEventResponse("success")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Vessel detector started...")
    app.run(50051)
