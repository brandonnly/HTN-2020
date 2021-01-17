import time
import os
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
        data = {"token": os.getenv("DROPBASE_API_KEY")}
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
        data = open('file.csv', 'rb')
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
        return response.json()


def database_query(table: str):
    """
    Queries the database table
    :param table: name of the table to query
    :return: json of the query
    """
    header = {"Authorization": os.getenv("DROPBASE_ACCESS_KEY")}
    response = requests.get(f'https://query.dropbase.io/5FdDQsCcujbAfvf3hWieyu/{table}', headers=header)
    return response.json()

