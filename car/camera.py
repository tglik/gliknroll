from picamera import PiCamera
from datetime import datetime
from threading import Timer
from os import path 

class CameraImpl(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = (640, 480)
        self.camera.framerate = 15

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

Camera = CameraImpl()
