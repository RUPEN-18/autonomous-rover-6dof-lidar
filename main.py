from rover.movement import RoverMovement
from rover.lidar import LiDAR
from rover.arm_control import RoboticArm
import time

def main():
    print("🚀 Starting Autonomous Rover System...")

    rover = RoverMovement()
    lidar = LiDAR()
    arm = RoboticArm()

    try:
        while True:
            # Step 1: Scan environment
            distance = lidar.get_distance()
            print(f"📡 Distance: {distance} cm")

            # Step 2: Decision making
            if distance < 30:
                print("⚠️ Obstacle detected!")

                rover.stop()
                time.sleep(1)

                rover.turn_left()
                time.sleep(1)

            else:
                rover.move_forward()

            # Step 3: Example arm action (demo)
            if distance < 15:
                print("🦾 Object very close - picking...")
                rover.stop()
                arm.pick_object()
                time.sleep(2)

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n🛑 Stopping Rover...")
        rover.stop()

if __name__ == "__main__":
    main()
