def turn_fan_on():
    # Turn the fan on using GPIO
    from gpio_utils import turn_fan_on
    import yaml
    
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    turn_fan_on(config['fan_pin'])
    print("Fan is turned ON.")

def turn_fan_off():
    # Turn the fan off using GPIO
    from gpio_utils import turn_fan_off
    import yaml
    
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    turn_fan_off(config['fan_pin'])
    print("Fan is turned OFF.")

def run_fan_schedule():
    import yaml
    from gpio_utils import setup_gpio, cleanup_gpio
    
    # Load configuration
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    # Setup GPIO
    setup_gpio(config['fan_pin'])
    
    try:
        while True:
            turn_fan_on()
            time.sleep(config['run_duration'])
            turn_fan_off()
            time.sleep(config['shutdown_duration'])
    except KeyboardInterrupt:
        cleanup_gpio()
        print("\nFan controller stopped.")

if __name__ == "__main__":
    import time
    run_fan_schedule()