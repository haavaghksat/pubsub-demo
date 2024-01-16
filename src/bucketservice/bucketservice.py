from typing import Optional
from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
from dapr.clients import DaprClient
from dapr.clients.grpc._response import TopicEventResponse
import time
import random
import json
import logging
import os

app = App()
file_path = os.getenv("SHARED_FILE_PATH")


@app.subscribe(pubsub_name='pubsub', topic='reconstructed_data')
# Subscription using GRPC
def sorted_data(event: v1.Event) -> Optional[TopicEventResponse]:
    logging.info(f"Bucketservice received an event with data: {str(event.Data())}")
    # Process the data
    with open(file=file_path+"/data.bin", mode='w') as f:
        f.writelines(str(event.Data()))
    time.sleep(3)
    logging.info("Bucketservice saved data to shared directory. Waiting for output file to be written")

    while not os.path.exists(file_path+"/output.bin"):
        time.sleep(10)

    if os.path.isfile(file_path+"/output.bin"):
        logging.info(f"Found output. Saving to storage")
        time.sleep(1)
        with open(file_path+"/output.bin", 'rb') as f:
            output_data = f.read()

    else:
        raise ValueError("%s isn't a file!" % file_path)

    with DaprClient() as dapr_client:
        # Publish to reconstructed_data topic
        logging.info(f"Completed processing data")
        processed_data = random.randbytes(20)
        payload = {"data": str(output_data)}
        payload_json = json.dumps(payload).encode('utf-8')
        dapr_client.publish_event(pubsub_name='pubsub',
                                  topic_name='processed_data',
                                  data=payload_json,
                                  data_content_type='application/json',
                                  )
        logging.info(f"Completed reconstruction on data. Sending message to reconstructed_data topic with contents: {payload_json}")
    return TopicEventResponse("success")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Bucketservice started...")
    app.run(50051)
