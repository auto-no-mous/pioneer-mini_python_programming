# Скрипт реализует периодическое мигание диодами, как у самолета
from pioneer_sdk import Pioneer
import time

low = 20
high = 255

if __name__ == '__main__':
    print('drone lights enabled')
    pioneer_mini = Pioneer()
    while True:
        # боковые огни
        pioneer_mini.led_control(led_id=0, r=low, g=0, b=0)
        pioneer_mini.led_control(led_id=3, r=0, g=low, b=0)
        # задние огни
        pioneer_mini.led_control(led_id=1, r=low, g=low, b=low)
        pioneer_mini.led_control(led_id=2, r=low, g=low, b=low)
        time.sleep(0.5)
        pioneer_mini.led_control(led_id=1, r=high, g=high, b=high)
        pioneer_mini.led_control(led_id=2, r=high, g=high, b=high)
        time.sleep(0.1)
        pioneer_mini.led_control(led_id=1, r=low, g=low, b=low)
        pioneer_mini.led_control(led_id=2, r=low, g=low, b=low)
        time.sleep(0.1)
        pioneer_mini.led_control(led_id=1, r=high, g=high, b=high)
        pioneer_mini.led_control(led_id=2, r=high, g=high, b=high)
        time.sleep(0.1)
        pioneer_mini.led_control(led_id=1, r=low, g=low, b=low)
        pioneer_mini.led_control(led_id=2, r=low, g=low, b=low)
        pioneer_mini.led_control(led_id=0, r=high, g=0, b=0)
        pioneer_mini.led_control(led_id=3, r=0, g=high, b=0)
        time.sleep(0.1)
        pioneer_mini.led_control(led_id=0, r=low, g=0, b=0)
        pioneer_mini.led_control(led_id=3, r=0, g=low, b=0)
        time.sleep(0.1)
        pioneer_mini.led_control(led_id=0, r=high, g=0, b=0)
        pioneer_mini.led_control(led_id=3, r=0, g=high, b=0)
        time.sleep(0.1)