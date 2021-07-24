# AltSight

From the perspective of someone who is visually impaired, the world seems to be a bit different but with the power of technology, we can change that. Using state-of-the-art (Google cloud vision in this case) object detection algorithms, their worldview can be improvised. AltVision is a custom, and portable object recognition device that can be worn as a cap, and can be connected to most audio devices. This wearable will play out the names of objects that are encountered by the user, who is supposedly visually impaired in this case.

## Hardware Requirements

+ Raspberry Pi
+ Pi Camera 5 MP
+ USB Type C Charger / 18650 Li-Ion Battery with adapter
+ Hat/Adjustable on-head wearable support

## Software Requirements

+ Thonny
+ Python3
+ Google Cloud Python library
+ espeak

## Installation

Python3 and Thonny are present by default in a Raspberry Pi
+ espeak
```
sudo apt-get install espeak python-espeak
```
+ Google Cloud Vision
```
pip install google-cloud-vision
```

## Relevant Links

Devpost: https://devpost.com/software/altsight
<br>Demo Video: https://youtu.be/4nYoSJ8HOBc
