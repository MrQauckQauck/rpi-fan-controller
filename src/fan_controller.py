def turn_fan_on():
    # Code to turn the fan on at full power
    print("Fan is turned ON.")

def turn_fan_off():
    # Code to turn the fan off
    print("Fan is turned OFF.")

def run_fan_schedule():
    while True:
        turn_fan_on()
        time.sleep(7200)  # Run for 2 hours
        turn_fan_off()
        time.sleep(10800)  # Shut down for 3 hours

if __name__ == "__main__":
    import time
    run_fan_schedule()