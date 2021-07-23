import os
import io

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
