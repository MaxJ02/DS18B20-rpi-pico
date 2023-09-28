import time
import machine
import onewire, ds18x20

# the device is connected to GPIO16
dat = machine.Pin(16) #placeholder to test the code, will be loaded from the json file later

# creates the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))


# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)


id = ""
for b in machine.unique_id():
  id += "{:02x}".format(b)

sensor_id = hex(int.from_bytes(b'(\xabG8N \x01\x0c', 'little'))[2:]


# loop 10 times and print all temperatures
for i in range(10):
    ds.convert_temp()
    time.sleep_ms(750) #placeholder, to be changed to read from config file later
    for rom in roms:
        print(id, sensor_id, ds.read_temp(rom), end=' ') # Needs adjustments
    print()
