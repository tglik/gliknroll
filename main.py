from controller.controls import Controls
from car.drive import Drive
from car.camera import Camera
from perception.ball import identify_yellow_ball

class CommonDriveActions(object):

    def __init__(self):
        self.driveon = False
        self.vid_duration = 10.0

    def onkey(self, key):
        if key == "B":
            self.driveon = not self.driveon
            print("Drive:", self.driveon)
        elif key=="Y":
            filename = Camera.capture()
            print("Capture: ", filename)
        elif key=="A":
            filename = Camera.record(self.vid_duration)
            print("Record: ", filename)
        elif key=="X":
            # catch ball
            frame = Camera.capture_mem()
            x,y,r = identify_yellow_ball(frame)
            adir, dist = (Camera.convert_x_to_dir(x), Camera.convert_radius_to_dist(r))
            print("Chase: ", adir, dist)
            #Drive.chase_obj(dir, dist)

        return True

    def onspeed(self, speed):
        print("Speed:", speed)
        if self.driveon:
            Drive.set_speed(speed)
        return True

    def ondir(self, direction):
        print("Dir:", direction)
        if self.driveon:
            Drive.set_dir(direction)
        return True

    def run(self):
        Controls.run_loop(self.onkey, self.onspeed, self.ondir)


def main():
    # TODO: wait for controller to connect
    Controls.setup()

    actor = CommonDriveActions()
    print("Starting event loop")
    actor.run()
    print("Done")


if __name__=="__main__":
    main()
