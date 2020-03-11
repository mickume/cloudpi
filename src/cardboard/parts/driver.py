
import time, math
from adafruit_motorkit import MotorKit

MOTOR_MAX_FORWARD = 1.0
MOTOR_MAX_REVERSE = -1.0
RADIANS_DEGREES = 57.3

def abs(f):
    if f < 0:
        return f * -1
    return f

def constrain(value, min, max):
    if value < min :
        return min
    if value > max :
        return max
    else:
        return value

# https://github.com/zlite/OpenMVrover/blob/master/linefollowing.py
class Driver:
    def __init__(self):
        # controller input
        self.throttle = 0.0
        self.angle = 0.0
        # motor parameters
        self.ml = 0.0 # motor speed
        self.mr = 0.0
        self.tl = 1.0 # motor trim
        self.tr = 1.0
        # drive control parameters
        self.steering_direction = 1   # use this to reverse the steering if your car goes in the wrong direction
        self.steering_gain = 1.0  # calibration for your car's steering sensitivity
        self.steering_center = 0  # set to your car's steering center point
        # motor stuff
        self.drive = True
        self.kit = MotorKit()
        self.stop()

    # parts stuff
    def update(self):
        while self.drive:
            time.sleep(0.2)
            
        self.stop()

    def run_threaded(self, throttle, angle):
        self.throttle = throttle
        self.angle = angle    
        return self.steer(throttle, angle)
        
            
    def shutdown(self):
        print("Stopping the engine")
        self.throttle = 0.0
        self.drive = False
        self.stop()

    #
    # engine control
    #

    def steer(self, throttle, angle):
        
        # simple step function
        da = abs(angle)
        inc = 0.03
        if da > 0.1 and da < 0.2:
            inc = inc * 1.5
        elif da >= 0.2:
            inc = inc * 2
        
        if angle < 0: # turn left
            ml = throttle - inc
            mr = throttle + inc
        else:
            ml = throttle + inc
            mr = throttle - inc

        #print ("motors ", throttle, angle, ml, mr)
        self.set_left(ml)
        self.set_right(mr)

        return ml, mr
        
    # stop the engine
    def stop(self):
        self.set_left(0.0)
        self.set_right(0.0)

    # set left motor speed
    def set_left(self, s):
        if self.ml == s:
            return
        if s < MOTOR_MAX_REVERSE:
            self.ml = MOTOR_MAX_REVERSE
        elif s > MOTOR_MAX_FORWARD:
            self.ml = MOTOR_MAX_FORWARD
        else:
            self.ml = s

        self.kit.motor2.throttle = self.ml * self.tl

    # set right motor speed
    def set_right(self, s):
        if self.mr == s:
            return
        if s < MOTOR_MAX_REVERSE:
            self.mr = MOTOR_MAX_REVERSE
        elif s > MOTOR_MAX_FORWARD:
            self.mr = MOTOR_MAX_FORWARD
        else:
            self.mr = s

        self.kit.motor1.throttle = self.mr * self.tr

