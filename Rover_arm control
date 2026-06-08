from adafruit_servokit import ServoKit
import time

class RoboticArm:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        print("🦾 Robotic Arm Ready")

    def pick_object(self):
        print("🤖 Picking object...")

        # Example movement sequence
        self.kit.servo[0].angle = 90
        time.sleep(0.5)

        self.kit.servo[1].angle = 120
        time.sleep(0.5)

        self.kit.servo[2].angle = 60
        time.sleep(0.5)

        # Close gripper
        self.kit.servo[5].angle = 30
        time.sleep(1)

        print("✅ Object picked")
