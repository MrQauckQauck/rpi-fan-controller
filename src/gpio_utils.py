def setup_gpio(pin):
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

def turn_fan_on(pin):
    import RPi.GPIO as GPIO
    GPIO.output(pin, GPIO.HIGH)

def turn_fan_off(pin):
    import RPi.GPIO as GPIO
    GPIO.output(pin, GPIO.LOW)

def cleanup_gpio():
    import RPi.GPIO as GPIO
    GPIO.cleanup()