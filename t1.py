from machine import Pin, SPIfrom ili9163 import ILI9163_SPI,ILI9163import ujsonimport urequestsimport framebufimport _thread
import gui
main_show=0spi = SPI(1,baudrate=26000000,sck=Pin(33), mosi=Pin(25),miso=Pin(4))
ili = ILI9163_SPI(128, 160, spi, res=Pin(27), dc=Pin(26), cs=Pin(4))ili.fill(0xFFFF)ili.fill_rect(5,5,56,50,ili.brg(r=255))ili.show()f=open("weather/0.bin")imgbyte=f.read()img=framebuf.FrameBuffer(bytearray(imgbyte),60,60,framebuf.RGB565)ili.blit(img,0,0)ili.show()
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
