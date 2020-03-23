#!usr/bin/env python3

import rospy
from std_msgs.msg import String

def simple_cb(val): #инициализируем функцию callback c именем simple_cb
    print(val)

def main():
    rospy.init_node('subscriber_node') #инициальизируем данную ноду с именем subscriber_node
    rospy.Subscriber('/talker', String, simple_cb) #создаём сабскрайбер, который принимает значения типа String из топика с именем /talker и потом отправляет эти данные в функцию callback с именем simple_cb
    rospy.spin() #заставляем функцию main работать бесконечно циклично

if __name__ == '__main__':
    main()