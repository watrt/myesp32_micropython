from machine import Pin, SPI
import gui
main_show=0
ili = ILI9163_SPI(128, 160, spi, res=Pin(27), dc=Pin(26), cs=Pin(4))
ili.fill(0xFFFF)
ui=gui.UI(ili)
for i in range(100):
  ui.ProgressBar(30,30,70,10,i)
  ui.stripBar(10,10,10,70,i,0,0)
  ili.show()
  time.sleep_ms(50)

ili.fill(0xFFFF)
ui.qr_code('http://www.163.com',20,20)
ili.show()

ili.fill(0xFFFF)
clock=gui.Clock(ili,64,60,40)
clock.settime()
clock.drawClock()
ili.show()