import os
import io
from picamera import PiCamera

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Downloads/cognitio-7378d-f0c72d841d75.json"

camera = PiCamera()
camera.capture('live.jpg')

def detect(img):
  from google.cloud import vision
  client = vision.ImageAnnotatorClient()
  file_name = os.path.abspath(img)
  with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
  image = vision.Image(content=content)
  response = client.label_detection(image=image)
  labels = response.label_annotations
  return labels

labels = detect('live.jpg')
print(labels)

for i in labels:
  print(i.description)
