from machine import ADC
from time import sleep

adc = ADC (1)

while True:
    val = adc.read_u16()
    val1 = val * 3.3
    val2 = val1/65535
    V1 = val2/0.01    
    print("la temperatura es de {:.2f}".format(V1))
    sleep(.1)

