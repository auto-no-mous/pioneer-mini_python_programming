# Доработка предыдущей задачи, коптер всегда поворачивается в ту сторону,
# куда он летит
from pioneer_sdk import Pioneer
import time
import math


def wait(pioneer_mini):
    while not pioneer_mini.point_reached():
        pass


def led_flicker(pioneer_mini, r, g, b):
    pioneer_mini.led_control(r=r, g=g, b=b)
    time.sleep(0.1)
    pioneer_mini.led_control(r=0, g=0, b=0)
    time.sleep(0.1)
    pioneer_mini.led_control(r=r, g=g, b=b)
    time.sleep(0.1)
    pioneer_mini.led_control(r=0, g=0, b=0)


if __name__ == '__main__':
    # вычиляем углы поворота
    east = math.radians(90)
    west = math.radians(-90)
    south = math.radians(180)
    north = math.radians(0)

    # поднимаем квадрокоптер
    print('start')
    pioneer_mini = Pioneer()
    pioneer_mini.arm()
    led_flicker(pioneer_mini, 255, 0, 0)
    pioneer_mini.takeoff()
    pioneer_mini.le

    # North
    pioneer_mini.go_to_local_point(x=0, y=0.5, z=1, yaw=north)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)

    # North - east
    pioneer_mini.go_to_local_point(x=float(0.5), y=float(0.5), z=float(1), yaw=west)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)

    # South - east
    pioneer_mini.go_to_local_point(x=float(0.5), y=float(-0.5), z=float(1), yaw=south)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)

    # South - west
    pioneer_mini.go_to_local_point(x=float(-0.5), y=float(-0.5), z=float(1), yaw=east)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)

    # North - west
    pioneer_mini.go_to_local_point(x=float(-0.5), y=float(0.5), z=float(1), yaw=north)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)

    # North again
    pioneer_mini.go_to_local_point(x=float(0), y=float(0.5), z=float(1), yaw=west)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)

    # Центр, а затем разворот
    pioneer_mini.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=south)
    wait(pioneer_mini)
    led_flicker(pioneer_mini, 0, 255, 0)
    pioneer_mini.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=east)
    wait(pioneer_mini)
    pioneer_mini.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=north)
    wait(pioneer_mini)

    # приземляемся
    pioneer_mini.land()
    led_flicker(pioneer_mini, 255, 0, 0)
    pioneer_mini.disarm()
