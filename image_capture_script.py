from picamera2 import MappedArray, Picamera2
from picamera2.devices import IMAX500
from picamera2.devices.imx500 import (NetworkIntrinsics,
                                       postprocess_nanodet_detection)


import os
import subprocess


#rpicam-jpeg --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json --output test.jpeg
#rpicam-jpeg --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json --output test.jpeg

#os.system(rpicam-jpeg --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json --output test.jpeg)

