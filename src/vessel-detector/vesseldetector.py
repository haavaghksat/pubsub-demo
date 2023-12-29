from dapr.clients import DaprClient
import logging
import time
import json
import random 
from flask import Flask, request
import logging

app = Flask(__name__)

@app.route('/reconstructed_data', methods=['POST'])
def reconstructed_data():
    data = request.json
    logging.info(f"Received data: {data}")
    time.sleep(3)
    # Dapr subscribes to messages using gRPC by default.
    with DaprClient() as dapr_client:
        logging.info(f"Received message: {data}")
        # detect_vessel
        logging.info(f"Completed vessel detection on data")
        payload = {"vessel": random.randint(1, 100)}
        payload_json = json.dumps(payload).encode('utf-8')
        dapr_client.publish_event(pubsub_name='pubsub',
            topic_name='detected_vessels',
            data=payload_json,
            data_content_type='application/json',
        )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5001)