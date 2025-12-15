#!/usr/bin/env python3
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge


class UserPositionDetector(Node):
    def __init__(self):
        super().__init__('user_position_detector')

        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.callback, 10)
        self.publisher = self.create_publisher(
            Int32, '/user_position_code', 10)

        self.bridge = CvBridge()
        self.face_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
        # Stability tracking
        self.last_position = -1
        self.position_count = 0

    def callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = self.face_detector.detectMultiScale(gray, 1.2, 5)
        
        if len(faces) == 0:
            self.last_position = -1  # No face → stop publishing
            self.position_count = 0
            return
        
        # Use largest confident face
        (x, y, w, h) = max(faces, key=lambda f: f[2]*f[3])
        face_center_x = x + w / 2
        width = frame.shape[1]
        
        if face_center_x < width * 0.25:
            position = 0  # left  
        elif face_center_x < width * 0.75:
            position = 1  # center
        else:
            position = 2  # right
        
        # Only publish if position stable for 3 frames
        if position == self.last_position:
            self.position_count += 1
        else:
            self.position_count = 1
            self.last_position = position
        
        if self.position_count >= 3:
            msg_out = Int32()
            msg_out.data = position
            self.publisher.publish(msg_out)

def main(args=None):
    rclpy.init(args=args)
    node = UserPositionDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
