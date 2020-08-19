from test import test_celery
import time
images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]
image_ids = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

for image, image_id in zip(images, image_ids):
    test_celery.delay(image, "EASY_OCR", image_id)
    time.sleep(8)
    #test_celery.delay(image, "DENSECAP", image_id)
