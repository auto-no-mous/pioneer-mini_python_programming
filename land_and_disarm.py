from pioneer_sdk import Pioneer


if __name__ == '__main__':
    pioneer_mini = Pioneer()
    pioneer_mini.land()
    pioneer_mini.disarm()
    pioneer_mini.led_control(r=0, g=0, b=0)
    print("pioneer off")