# Квадрокоптер летит по траектории квадрата, центр
# которого находится в точке взлета, и возвращается в исходную точку
from pioneer_sdk import Pioneer
import time

if __name__ == '__main__':
    print('start')
    pioneer_mini = Pioneer()
    pioneer_mini.arm()
    pioneer_mini.takeoff()
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=0, y=0.5, z=1, yaw=0)
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=float(0.5), y=float(0.5), z=float(1), yaw=(float(0)))
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=float(0.5), y=float(-0.5), z=float(1), yaw=(float(0)))
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=float(-0.5), y=float(-0.5), z=float(1), yaw=(float(0)))
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=float(-0.5), y=float(0.5), z=float(1), yaw=(float(0)))
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=float(0), y=float(0.5), z=float(1), yaw=(float(0)))
    time.sleep(2)
    pioneer_mini.go_to_local_point(x=float(0), y=float(0), z=float(1), yaw=(float(0)))
    time.sleep(2)
    pioneer_mini.land()
    pioneer_mini.disarm()
