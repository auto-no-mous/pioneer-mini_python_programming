from pioneer_sdk import Pioneer
import time
import math
from multiprocessing import Process
import threading


def wait(drone):
    while not drone.point_reached():
        pass


def flight_lights(drone, start=1):
    if start == 0:
        drone.led_control(r=0, g=0, b=0)
        print('drone lights disabled')
    else:
        low = 20
        high = 255
        print('drone lights enabled')
        while True:
            # боковые огни
            drone.led_control(led_id=0, r=low, g=0, b=0)
            drone.led_control(led_id=3, r=0, g=low, b=0)
            # задние огни
            drone.led_control(led_id=1, r=low, g=low, b=low)
            drone.led_control(led_id=2, r=low, g=low, b=low)
            time.sleep(0.5)
            drone.led_control(led_id=1, r=high, g=high, b=high)
            drone.led_control(led_id=2, r=high, g=high, b=high)
            time.sleep(0.1)
            drone.led_control(led_id=1, r=low, g=low, b=low)
            drone.led_control(led_id=2, r=low, g=low, b=low)
            time.sleep(0.1)
            drone.led_control(led_id=1, r=high, g=high, b=high)
            drone.led_control(led_id=2, r=high, g=high, b=high)
            time.sleep(0.1)
            drone.led_control(led_id=1, r=low, g=low, b=low)
            drone.led_control(led_id=2, r=low, g=low, b=low)
            drone.led_control(led_id=0, r=high, g=0, b=0)
            drone.led_control(led_id=3, r=0, g=high, b=0)
            time.sleep(0.1)
            drone.led_control(led_id=0, r=low, g=0, b=0)
            drone.led_control(led_id=3, r=0, g=low, b=0)
            time.sleep(0.1)
            drone.led_control(led_id=0, r=high, g=0, b=0)
            drone.led_control(led_id=3, r=0, g=high, b=0)
            time.sleep(0.1)


def square_flight(drone):
    # вычиляем углы поворота
    east = math.radians(90)
    west = math.radians(-90)
    south = math.radians(180)
    north = math.radians(0)

    # поднимаем квадрокоптер
    print('square flight starts')
    drone.arm()
    drone.takeoff()

    # North
    drone.go_to_local_point(x=0, y=0.5, z=1, yaw=north)
    wait(drone)

    # North - east
    drone.go_to_local_point(x=float(0.5), y=float(0.5), z=float(1), yaw=west)
    wait(drone)

    # South - east
    drone.go_to_local_point(x=float(0.5), y=float(-0.5), z=float(1), yaw=south)
    wait(drone)

    # South - west
    drone.go_to_local_point(x=float(-0.5), y=float(-0.5), z=float(1), yaw=east)
    wait(drone)

    # North - west
    drone.go_to_local_point(x=float(-0.5), y=float(0.5), z=float(1), yaw=north)
    wait(drone)

    # North again
    drone.go_to_local_point(x=float(0), y=float(0.5), z=float(1), yaw=west)
    wait(drone)

    # Центр, а затем разворот
    drone.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=south)
    wait(drone)
    drone.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=east)
    wait(drone)
    drone.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=north)
    wait(drone)

    # приземляемся
    drone.land()
    drone.disarm()


if __name__ == '__main__':
    pioneer_mini = Pioneer()
    lights = threading.Thread(target=flight_lights, args=([pioneer_mini]))
    lights.start()
    flight = threading.Thread(target=square_flight, args=([pioneer_mini]))
    flight.start()
