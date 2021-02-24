import utime, machine, onewire, ds18x20

TempPin = machine.Pin(28)
ds = ds18x20.DS18X20(onewire.OneWire(TempPin))
roms = ds.scan()

while True:
    print('temperatures:', end=' ')
    ds.convert_temp()
    utime.sleep(0.5)
    for rom in roms:
        print(ds.read_temp(rom), "C")