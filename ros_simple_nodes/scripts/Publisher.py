#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node('pub_node') #инициализируем ноду с именем pub_node
pub = rospy.Publisher('/talker', String, queue_size=10) #создаём паблишер в данной ноде, который отправляет данные типа String в топик /talker и указываем queue_size означающее количество публикуемых сообщений за раз 

hz = rospy.Rate(10) #инициализируем задержку

while not rospy.is_shutdown():
    pub.publish('Hello my white master!')
    print('published')
    print(rospy.get_rostime())
    print(rospy.Time(1, 1))


    hz.sleep() #задержка на время hz
