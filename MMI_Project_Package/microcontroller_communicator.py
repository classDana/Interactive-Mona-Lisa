#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial
import time

class MicrocontrollerCommunicator(Node):
    def __init__(self):
        super().__init__('microcontroller_communicator')

        # /dev/ttyACM0 is the port of the Arduino
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(2)
        self.subscription = self.create_subscription(
            Int32,
            '/user_position_code',
            self.callback,
            10)

    def callback(self, msg):
        self.ser.write(f"{msg.data}\n".encode())

def main(args=None):
    rclpy.init(args=args)
    node = MicrocontrollerCommunicator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': 
    main()
