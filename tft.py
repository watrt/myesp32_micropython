


from machine import Pin, SPI
from ili9163 import ILI9163_SPI,ILI9163
import ujson
import urequests
import _thread
spi = SPI(baudrate=4000000,sck=Pin(27), mosi=Pin(26),miso=Pin(22))  #miso=Pin(4)是无交的因为必须配置所以乱写的
ili = ILI9163_SPI(128, 160, spi, Pin(25), Pin(33), Pin(22))

main_show=True
def getnowtime():
  import ntptime
  import machine
  ntptime.host="cn.ntppod.com"
  rtc=machine.RTC()
  ntptime.settime()
  
def showtime():
  ili.fill(0xFFFF)
  try:
    if rtc.datetime()[0]<2020:
      getnowtime()  #小于2020年就重新更新时间
    ili.fill_rect(5,5,56,50,ili.brg(r=255))
    ili.fill_rect(66,5,56,50,ili.brg(b=255))
    ili.fill_rect(5,60,118,50,ili.brg(g=255))
    ili.fill_rect(5,115,118,50,ili.brg(255,0,204))
    ili.text('%s' % nic.ifconfig()[0], 8, 120, 0xFFFF)
    ili.text('%s' % nic.ifconfig()[1], 8, 130, 0xFFFF)
    ili.text('%s' % nic.ifconfig()[2], 8, 140, 0xFFFF)
    ili.text('RAM:', 70, 18, 0xFFFF)
    ili.text('%sKb' % (gc.mem_free()//1024), 70, 30, 0xFFFF)
    ili.text('HI!', 10, 16, ili.brg(b=255))
    ili.text('FUKUN!', 10, 26, ili.brg(b=255))
    ili.text('DATE:%s-%s-%s'%(rtc.datetime()[0],rtc.datetime()[1],rtc.datetime()[2]), 8, 73, ili.brg(b=255))
    ili.text('TIME:%s:%s:%s'%(rtc.datetime()[4],rtc.datetime()[5],rtc.datetime()[6]), 8, 88, ili.brg(b=255))
  except:
    ili.text('ERROR!!', 10, 26, ili.brg(b=255))
  finally:
    ili.show()

def showweather():
  ili.fill(0xFFFF)
  try:
    response = urequests.get('http://t.weather.sojson.com/api/weather/city/101270401')
    weather = ujson.loads(response.text)
    ili.fill_rect(5,5,118,90,ili.brg(g=255))
    ili.text('shidu:%s' % weather['data']['shidu'], 10, 10, ili.brg(r=255))
    ili.text('pm25:%s' % weather['data']['pm25'], 10, 20, ili.brg(r=255))
    ili.text('pm10:%s' % weather['data']['pm10'], 10, 30, ili.brg(r=255))

    ili.text('wendu:%s' % weather['data']['wendu'], 10, 40, ili.brg(r=255))
    ili.text('cityInfo:%s' % weather['cityInfo']['city'], 10, 50, ili.brg(r=255))
    ili.text('ZhiShu:%s' % weather['data']['yesterday']['aqi'], 10, 60, ili.brg(r=255))
    ili.text('citykey:%s' % weather['cityInfo']['citykey'], 10, 70, ili.brg(r=255))
    ili.text('updateTime:%s' % weather['cityInfo']['updateTime'], 10, 80, ili.brg(r=255))
    
    ili.fill_rect(5,100,118,60,ili.brg(r=255))
    ili.text('sunrise:%s' % weather['data']['yesterday']['sunrise'], 10, 110, ili.brg(b=255))
    ili.text('sunset:%s' % weather['data']['yesterday']['sunset'], 10, 120, ili.brg(b=255))
  except:
    ili.text('ERROR!!', 10, 26, ili.brg(b=255))
  finally:
    ili.show()

def mainshow(agv):
    global main_show
    while main_show:
      showtime()
      time.sleep(4)
      
      showweather()
      time.sleep(4)
      
    _thread.exit()
_thread.start_new_thread(mainshow,(1,))

