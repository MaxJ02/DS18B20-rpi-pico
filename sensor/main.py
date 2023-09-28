import time
import machine
import onewire, ds18x20
import ujson

with open('config.json', 'r') as f:
    config = ujson.load(f)

dat_pin_number = config.get('pin', 16)  # reads the pin number from the config file, defaults to 16
sleep_time = config.get('interval', 9) # reads the interval from the config file, defaults to 9 seconds

# The device is connected to GPIO16 
dat = machine.Pin(dat_pin_number)

# creates the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))


# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

# Reads the unique id of the device and converts it to a hex string
id = ""
for b in machine.unique_id():
  id += "{:02x}".format(b)


# loop to read the temperature from the sensor and print it to the console infinitely
while True:
    ds.convert_temp()
    time.sleep(sleep_time)
    for rom in roms:
        sensor_id = hex(int.from_bytes(rom, 'little'))[2:]
        print(id, sensor_id, ds.read_temp(rom), end=' ')
    print()