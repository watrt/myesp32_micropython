

import network
import machine
import time
import ntptime
try:
  nic = network.WLAN(network.STA_IF) # create station interface
  nic.active(True)       # activate the interface
  wifilist=[['028sd.com','88884444'],['ZCWH','00004157']]
  for info in wifilist:
    nic.connect(info[0],info[1]) # connect to an AP
    wificonut=10
    while nic.status()==1001 and wificonut>0:
      print("连接到：%s=>%s" % (info[0],wificonut))
      wificonut-=1
      time.sleep(1)

  print(nic.ifconfig())

  ntptime.host="cn.ntppod.com"
  rtc=machine.RTC()
  ntptime.settime()
  

except:
  
  rtc=machine.RTC()
finally:
  nic.ifconfig()
  exec(open('./tft.py').read(),globals())

