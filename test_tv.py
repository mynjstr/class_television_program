#call class tv
#Import TV from class_tv.py
from class_tv import TV
#Create a TV object named tv1 and tv2 with parameters
tv1 = TV('tv1', 121, 10, True)
tv2 = TV('tv2', 6, 7, False)

#tv1
tv1.channel_up_1()
tv1.set_channel(35)
tv1.channel_down_1()
tv1.channel_down_1()
tv1.channel_down_1()
tv1.channel_down_1()
tv1.channel_down_1()
tv1.set_volume(8)
tv1.volume_down()
tv1.volume_down()
tv1.volume_down()
tv1.volume_down()
tv1.volume_down()

#tv2
tv2.turn_on()
tv2.channel_down_1()
tv2.set_channel(1)
tv2.channel_up_1()
tv2.channel_up_1()
tv2.volume_down
tv2.volume_down()
tv2.volume_down()
tv2.volume_down()
tv2.volume_down()
#Show the result