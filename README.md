# rpi-fan-controller

So, I can just imagine that 99.75% of people are going to look at this and just shake their heads, maybe even screaming at their screens like, 'Why on earth would you do something so dumb?!' Some might even say, 'It’s a pointless idea that doesn’t even need fans!' And you know what? You’re probably right. But hey, sometimes it’s just fun to do dumb little things and mess around. Who needs logic when you’ve got curiosity and a dash of chaos?


This project is designed to control a fan using a Raspberry Pi 5. The fan will operate on a schedule, running at full power for 2 hours, followed by a 3-hour shutdown, and then running again for another 2 hours.

## Project Structure

```
rpi-fan-controller
├── src
│   ├── fan_controller.py      # Main logic for controlling the fan
│   ├── scheduler.py           # Manages timing for fan operation
│   └── gpio_utils.py          # Utility functions for GPIO interaction
├── config
│   └── config.yaml            # Configuration settings for the fan controller
├── scripts
│   └── install_service.sh      # Script to install the fan controller as a service
├── tests
│   └── test_fan_controller.py  # Unit tests for fan control logic
├── requirements.txt            # Python dependencies for the project
├── README.md                   # Project documentation
└── LICENSE                     # Licensing information
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd rpi-fan-controller
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the fan controller:**
   Edit the `config/config.yaml` file to set the GPIO pin number for the fan and adjust any timing intervals if necessary.

4. **Run the fan controller:**
   You can run the fan controller script directly:
   ```bash
   python src/fan_controller.py
   ```

5. **Install as a service (optional):**
   If you want the fan controller to run in the background, use the provided script:
   ```bash
   ./scripts/install_service.sh
   ```

## Usage

The fan controller will automatically manage the fan operation based on the defined schedule. Ensure that the fan is connected to the specified GPIO pin on the Raspberry Pi.

## Testing

To run the unit tests for the fan controller, execute:
```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
