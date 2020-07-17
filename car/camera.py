from picamera import PiCamera, PiRGBArray
from datetime import datetime
from threading import Timer
from os import path 


RESOLUTION = (640, 480)
FOV = 750.0

class CameraImpl(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = RESOLUTION
        self.camera.framerate = 15

        self.rawCapture = PiRGBArray(camera, size=RESOLUTION)


        self.outdir = "/tmp"

    def capture(self):
        filename = path.join(self.outdir, datetime.now().strftime("%Y-%m-%d-%H:%M:%S.jpg"))
        self.camera.capture(filename)
        return filename

    def record(self, duration):
        filename = path.join(self.outdir, datetime.now().strftime("%Y-%m-%d-%H:%M:%S.h264"))
        self.camera.start_recording(filename)
        timer = Timer(duration, self.camera.stop_recording)
        timer.start()
        return filename

    def capture_mem(self):
        self.camera.capture(self.rawCapture, format="bgr")
        return self.rawCapture.array

    def convert_x_to_dir(self, x):
        return float(x) / RESOLUTION[0] * 2 - 1

    def convert_radius_to_dist(self, radius_in_pixels, obj_in_meters):
        return FOV * obj_in_meters / radius_in_pixels


Camera = CameraImpl()
