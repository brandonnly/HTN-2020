import time

import requests


class Job:
    def __init__(self):
        self.upload_url = None
        self.job_id = None
        self.get_presigned()

    def get_presigned(self):
        """
        Get presigned url for uploading file to dropbase
        :return:
        """
        data = {"token": "gpri9HrjnoWR7peSoK9ghc"}
        processing = requests.post(
            "https://api2.dropbase.io/v1/pipeline/generate_presigned_url",
            data=data)

        return_data = processing.json()

        print(f"Got Presigned URL | URL: {return_data['upload_url']} - "
              f"Job ID: {return_data['job_id']}")

        self.upload_url = return_data["upload_url"]
        self.job_id = return_data["job_id"]

    def run_pipeline(self):
        """
        Upload file and run pipeline
        :return:
        """
        headers = {
            'Content-Type': 'text/plain',
        }
        data = open('devices.json', 'rb')
        response = requests.put(self.upload_url, data=data)
        print(response)
        print("response sent!")

    def get_job_status(self):
        """
        Returns the status code of the job
        :return:
        """
        response = requests.get("https://api2.dropbase.io/v1/pipeline/run_pipeline", data={"job_id": self.job_id})
        print(f"\nStatus Code: {response}\nMessage: {response.json()}")


test = Job()
test.run_pipeline()
while True:
    time.sleep(3)
    test.get_job_status()
