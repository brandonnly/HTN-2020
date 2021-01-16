import requests, json


def get_presigned():
    """
    Get presigned url for uploading file to dropbase
    :return:
    """
    data = { "token": "DDmSEyrziXmyLqqbnm9D93"}
    processing = requests.post(
        "https://api2.dropbase.io/v1/pipeline/generate_presigned_url", data=data)
    returnData = processing.json()
    print(f"{returnData['upload_url']} | {returnData['job_id']}")
    return returnData["upload_url"], returnData["job_id"]


def run_pipeline():
    """
    Upload file and run pipeline
    :return:
    """
    upload_url, job_id = get_presigned()
    processing = requests.put(upload_url, data=file('untitled.csv','rb').read())
