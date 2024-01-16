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
logging.info("Vessel detector started...")


@app.subscribe(pubsub_name='pubsub', topic='reconstructed_data')
# Subscription using GRPC
def reconstructed_data(event: v1.Event) -> Optional[TopicEventResponse]:
    data = event.Data()
    logging.info(f"Received data reconstructed data: {data}")
    logging.info(f"Performing vessel detection on data....")
    time.sleep(3)
    n_vessels = np.random.randint(0, 10)
    vessels = [zip(np.random.rand(n_vessels), np.random.rand(n_vessels))]

    logging.info(f"Completed detecting vessels. Found {n_vessels} vessels")
    with DaprClient() as dapr_client:
        # Send message
        payload = {"Vessels": vessels}
        payload_json = json.dumps(payload).encode('utf-8')
        dapr_client.publish_event(pubsub_name='pubsub',
                                  topic_name='detected_vessels',
                                  data=payload_json,
                                  data_content_type='application/json',
                                  )
    logging.info(f"Published message to detected_vessels topic with data: {payload_json}")
    return TopicEventResponse("success")


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    app.run(50053)
