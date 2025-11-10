import subprocess

def run_pinctrl_command(command):
    try:
        subprocess.run(['sudo', 'pinctrl'] + command.split(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running pinctrl command: {e}")

def setup_gpio(pin):
    # Pi 5 doesn't need traditional GPIO setup for the fan
    pass

def turn_fan_on(pin):
    # Use pinctrl to turn on the fan
    run_pinctrl_command('FAN_PWM op dl')

def turn_fan_off(pin):
    # Use pinctrl to turn off the fan
    run_pinctrl_command('FAN_PWM op dh')

def cleanup_gpio():
    # No cleanup needed for Pi 5 fan control
    pass