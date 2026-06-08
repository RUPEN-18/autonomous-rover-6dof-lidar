import RPi.GPIO as GPIO
import time

class RoverMovement:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.IN1 = 17
        self.IN2 = 18
        self.IN3 = 22
        self.IN4 = 23

        pins = [self.IN1, self.IN2, self.IN3, self.IN4]

        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def move_forward(self):
        print("➡️ Moving Forward")
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    def stop(self):
        print("⛔ Stopping")
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def turn_left(self):
        print("↩️ Turning Left")
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    def turn_right(self):
        print("↪️ Turning Right")
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
