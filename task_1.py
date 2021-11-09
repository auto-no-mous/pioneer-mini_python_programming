# Квадрокоптер поднимается, и пролетает 1 метр вперед,
# затем садится
from pioneer_sdk import Pioneer
import time

if __name__ == '__main__':
    print('start')
    pioneer_mini = Pioneer()
    pioneer_mini.arm()
    pioneer_mini.takeoff()
    pioneer_mini.go_to_local_point(x=0, y=1, z=1, yaw=0)
    time.sleep(2)
    pioneer_mini.land()
    pioneer_mini.disarm()
