from dotenv import load_dotenv
from my_celery.celery import celery_app
import requests
import redis
import time

load_dotenv()
REDIS_HOSTNAME = os.getenv("REDIS_HOSTNAME")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")


r = redis.StrictRedis(host=REDIS_HOSTNAME, port=REDIS_PORT,
                      password=REDIS_PASSWORD, ssl=True)
containers = {
    "EASY_OCR": "http://52.188.166.61:80/easyocr/",
    "KERAS_OCR": "url",
    "DENSECAP": "http://52.188.166.61:7000/uploadfile/"
}


@celery_app.task()
def test_celery(image, container, image_id):
    result = r.get(container)
    container_status = result.decode("utf-8")
    while container_status == "BUSY":
        result = r.get(container)
        container_status = result.decode("utf-8")
        print("in loop")
        print(image + " container busy", container, container_status)
        time.sleep(20)
    print("################### out of loop ####################")
    print("container free", container, container_status)
    print("***************************************************")
    print("sending image " + image + " to container " + container)
    print("***************************************************")
    # url = containers[container]
    #
    # payload = {'image_id': image_id}
    # files = [
    #     ('file', open(image, 'rb'))
    # ]
    #
    # response = requests.request("POST", url, data=payload, files=files)
    # print("response of " + container + image + " "+ str(response.text.encode('utf8')))
