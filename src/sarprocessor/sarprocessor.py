import os.path
import random
import time
import logging

file_path = os.getenv("SHARED_FILE_PATH")
input_file_name = file_path+"/data.bin"
output_file_name = file_path+"/output.bin"

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    logging.info("SAR processor running")
    while(1):
        while not os.path.exists(input_file_name):
            logging.info(f"SAR processor waiting for file")
            time.sleep(1)

        if os.path.isfile(input_file_name):
            logging.info(f"SAR processor received file")
            with open(file=input_file_name, mode="rb") as f:
                data = f.readline()
                logging.info(f"Processing file.....")
                time.sleep(10)
            with open(file=output_file_name, mode="w") as f:
                f.writelines(f"Processed_data{random.randint(0, 100)}")
                logging.info(f"Saved file as {output_file_name}")

        else:
            raise ValueError("%s isn't a file!" % input_file_name)
