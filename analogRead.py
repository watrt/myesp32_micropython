#Hardware Platform: FireBeetle-ESP32
#Result: read analog voltage of the IO interfaces.
#The info below shows that analogRead is available for the current version.
# A0/IO36   A1/IO39   A2/IO34   A3/IO35   A4/IO15
#There are 5 analog input interfaces (A0~A4) in FireBeetle-ESP32.
from machine import ADC,Pin
import time
adc0=ADC(Pin(34))               #create ADC object
while True:
  print("adc0=",adc0.read())    #Read ADC value
  time.sleep(0.1)
