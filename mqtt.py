from umqtt.simple import MQTTClientfrom machine import Pinimport ujsonimport urequestsimport networkimport timeSERVER = "www.028sd.net"CLIENT_ID = "esp32_01"TOPIC = b"/#"username='xk102'password='200000'state = 0c=Nonedef sub_cb(topic, msg):  global state  print((topic, msg))  try:    data = ujson.loads(msg.decode())    print(data)    if data['cmd'] == "clean":      print("清屏")      ili.fill(0xFFFF)      ili.show()    elif data['cmd'] == "strst":      print("写字")      ili.fill(0xFFFF)      line = int(data['line']) if "line" in data.keys() else 0      col = int(data['col']) if "col" in data.keys() else 0      print("行列:%d :%d" % (line,col))      ili.textst('%s' % (data['data']), col, line*13, ili.brg(r=255))      ili.show()    elif data['cmd'] == "toggle":      print("X")      # LED is inversed, so setting it to current state      # value will make it toggle  except Exception as e:    print(e)    print("未知指令")    try:  c = MQTTClient(CLIENT_ID, SERVER,0,username,password)     #create a mqtt client  c.set_callback(sub_cb)                    #set callback  c.connect()                               #connect mqtt  c.subscribe(TOPIC)                        #client subscribes to a topic  print("连接到 %s, 已订阅 %s topic" % (SERVER, TOPIC))  while True:    c.wait_msg()                            #wait message finally:  if(c is not None):    c.disconnect()