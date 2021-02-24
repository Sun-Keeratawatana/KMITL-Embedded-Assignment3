import machine, utime
from machine import Pin, time_pulse_us

class Sonic:
    
    def __init__(self, trig_pin=0, echo_pin=1):
        self.trigger = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN, Pin.PULL_DOWN)

    def send_pulse_and_wait(self):
        self.trigger.value(0)
        utime.sleep_us(5)
        self.trigger.value(1)
        utime.sleep_us(10)
        self.trigger.value(0)
        pulse_time = time_pulse_us(self.echo, 1, 30000)
        return pulse_time

    def distance(self):
        pulse_time = self.send_pulse_and_wait()
        cm = (pulse_time / 2) / 29.1
        return cm
    
while True:
    print("distance:", Sonic().distance(), "cm")
    utime.sleep(1)