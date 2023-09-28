# Raspberry Pi Pico Temperature Sensor

This project utilizes a Raspberry Pi Pico to read temperature data from a DS18x20 temperature sensor and print the readings to the console. The pin number for the sensor and the time interval for readings can be customized via a `config.json` file.

## 🛠️ Requirements

- Raspberry Pi Pico with MicroPython installed.
- DS18x20 Temperature Sensor.
- MicroPython Libraries:
  - `machine`
  - `onewire`
  - `ds18x20`
  - `ujson`
  
## 📁 File Structure

- `temp_sensor.py` - The main Python script to run.
- `config.json` - (Optional) A configuration file to set up the pin and interval for readings.

## 🚀 Getting Started

### 1. Install MicroPython

Ensure MicroPython is installed on your Raspberry Pi Pico. Follow the instructions [here](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython) if you haven't installed it yet.

### 2. Connect the DS18x20 Sensor

Connect the DS18x20 temperature sensor to the correct GPIO pin as per the sensor's datasheet.

### 3. Upload the Files

- Create a `temp_sensor.py` file and copy the provided code into this file.
- Optionally, create a `config.json` file with the pin number and interval:
