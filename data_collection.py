# Code for reading sensor data using RP2040
from machine import Pin, ADC
import network
import urequests
import time

# Define the ADC pins for voltage and current sensors
voltage_pin = ADC(0)
current_pin = ADC(1)

# Function to read voltage
def read_voltage():
    raw_voltage = voltage_pin.read_u16()
    voltage = raw_voltage * (3.3 / 65535) * 2  # multiplier is adjusted for voltage divider
    return voltage

# Function to read current
def read_current():
    raw_current = current_pin.read_u16()
    current = raw_current * (3.3 / 65535)  # To be  adjusted based on current sensor
    return current

# Function to send data to server
def send_data(voltage, current):
    url = "http://your-server-url/data"
    payload = {"voltage": voltage, "current": current}
    response = urequests.post(url, json=payload)
    print(response.text)

# Main loop
while True:
    voltage = read_voltage()
    current = read_current()
    send_data(voltage, current)
    time.sleep(1200)  # Data is sent every 20 minutes
