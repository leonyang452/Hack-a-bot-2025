from picamera2 import MappedArray, Picamera2
from picamera2.devices import IMAX500
from picamera2.devices.imx500 import (NetworkIntrinsics,
                                       postprocess_nanodet_detection)


import os



rpicam-jpeg --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json -o test.jpeg
