from time import sleep
from fan_controller import turn_fan_on, turn_fan_off

def run_fan_schedule():
    while True:
        turn_fan_on()  # Turn the fan on
        sleep(2 * 60 * 60)  # Run for 2 hours
        turn_fan_off()  # Turn the fan off
        sleep(3 * 60 * 60)  # Shut down for 3 hours

if __name__ == "__main__":
    run_fan_schedule()