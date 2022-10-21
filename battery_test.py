from machine import Pin, I2C, ADC
from utime import sleep
from oled import SSD1306_I2C

SCL_Pin = 15
SDA_Pin = 14
WIDTH =128
HEIGHT= 64

print("initialisiere Display, Pin und LED")
i2c=I2C(1,scl=Pin(SCL_Pin),sda=Pin(SDA_Pin),freq=200000)
display = SSD1306_I2C(WIDTH,HEIGHT,i2c)

Vin = ADC(27)
def open_circ():
    display.text('-BATTERY TESTER-', 0, 0)
    display.text('Ready to test...', 0, 16)
    display.show()

def measuring(adc_16_read):
    display.text('-BATTERY TESTER-', 0, 0)
    display.text('Measuring...', 0, 16)
    read_voltage=3.3*adc_16_read/65535
    read_voltage=round(read_voltage,2)
    display.text('Vin = '+str(read_voltage)+'V', 0, 32)
    display.show()

noise = 2000

while True:
    try:
        reading = Vin.read_u16()
        display.fill(0)
        if reading < noise:
            open_circ()
        else:
            measuring(reading)
        sleep(1)
    except OSError as e:
        machine.reset()
