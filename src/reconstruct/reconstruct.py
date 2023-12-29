from dapr.clients import DaprClient
import logging
import time 
import random
import json
from flask import Flask, request
import logging

app = Flask(__name__)

@app.route('/sorted_data', methods=['POST'])
def sorted_data():
    # Process the data
    data = request.json
    logging.info(f"Received data: {data}")
    time.sleep(3)

    with DaprClient() as dapr_client:
    # Subscribe to the topic
        logging.info(f"Completed reconstruction on data")
        payload = {"number": random.randint(1, 100)}
        payload_json = json.dumps(payload).encode('utf-8')
        dapr_client.publish_event(pubsub_name='pubsub',
            topic_name='reconstructed_data',
            data=payload_json,
            data_content_type='application/json',
        )
    return {}

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5001)