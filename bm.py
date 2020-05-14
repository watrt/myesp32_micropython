

import os
import machine 
from machine import Pin
import time
#p5 = Pin(5, Pin.IN)
#p5.irq(trigger=Pin.IRQ_FALLING,handler=func)
j=1
p34 = Pin(34, Pin.IN)
p35 = Pin(35, Pin.IN)


def func1(v):
  global j
  state = machine.disable_irq()
  time.sleep_us(10)
  if(v.value()==0):
    bm = p35.value()
    if bm==1:
      j+=1
    else:
      j-=1
    print(j)
  machine.enable_irq(state)

machine.freq()          # get the current frequency of the CPU
machine.freq(240000000) # set the CPU frequency to 240 MHz

p34.irq(trigger=Pin.IRQ_FALLING ,handler=func1)












