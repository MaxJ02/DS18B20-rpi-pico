# Raspberry Pi Pico Temperature Sensor

This project utilizes a Raspberry Pi Pico to read temperature data from a DS18x20 temperature sensor and print the readings to the console. The pin number for the sensor and the time interval for readings can be customized via the `config.json` file.

## 🛠️ Requirements

- Raspberry Pi Pico with MicroPython installed.
- DS18x20 Temperature Sensor.
- MicroPython Libraries:
  - `machine`
  - `onewire`
  - `ds18x20`
  - `ujson`
  
## 📁 File Structure

- `main.py`     - The main Python script to run.
- `config.json` -  A configuration file to set up the pin and interval for readings.

## 🚀 Getting Started

### 1. Install MicroPython

Ensure MicroPython is installed on your Raspberry Pi Pico. Follow the instructions [here](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython) if you haven't installed it yet.

### 2. Connect the DS18x20 Sensor

Connect the DS18x20 temperature sensor to the correct GPIO pin as per the sensor's datasheet.

### 3. Upload the Files

- Create a `main.py` file and copy the provided code into this file.
- Secondly, create a `config.json` file with the desired pin number and interval:


    Transfer both the main.py and config.json files to your Raspberry Pi Pico.

### 4. Running the Script

After uploading the files, navigate to the Python file via Thonny Python IDE or run the following command in the REPL prompt:

import main.py

## Expected Output 📈

The console should repeatedly display the unique id of the Raspberry Pi Pico, the sensor's id, and the temperature read from the sensor in the following format:


<pico_id> <sensor_id> <temperature>


### Troubleshooting 🛠️

    Verify that the sensor is securely and correctly connected.
    Ensure config.json is in the correct format and located in the same directory as main.py.
    Confirm the availability of all required libraries in your MicroPython environment.
    Update your MicroPython firmware if encountering any errors or discrepancies in displayed ids.
