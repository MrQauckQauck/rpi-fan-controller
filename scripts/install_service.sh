#!/bin/bash

# This script installs the fan controller as a systemd service on the Raspberry Pi.

SERVICE_FILE=/etc/systemd/system/rpi-fan-controller.service

# Create the service file
echo "[Unit]
Description=Raspberry Pi Fan Controller
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /path/to/rpi-fan-controller/src/fan_controller.py
WorkingDirectory=/path/to/rpi-fan-controller
StandardOutput=inherit
StandardError=inherit
Restart=always

[Install]
WantedBy=multi-user.target" | sudo tee $SERVICE_FILE

# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable rpi-fan-controller.service

# Start the service immediately
sudo systemctl start rpi-fan-controller.service

echo "Raspberry Pi Fan Controller service installed and started."