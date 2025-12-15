# Interactive-Mona-Lisa
## Introduction
Interactive Mona Lisa is a ROS2 and Arduino project that brings the famous painting to life. By combining computer vision, robotics, and my passion for art, I created a system where Mona Lisa’s eyes follow the viewer around the room. This project is my first exploration of blending art and technology, and it was an incredibly fun and inspiring experience to build.

<div align="center">
<img src="https://github.com/user-attachments/assets/9395ff10-5c6a-4e04-bba2-cca9ceb9d185" width="500" alt="Interactive Mona Lisa">
</div>

## Hardware Setup
### Hardware Components
- Arduino Uno R3 Controller Board
- SG90 Servo Motor
- Integrated Camera (PC)
- Any smartphone

### Connecting the Hardware with WSL
To connect USB devices to WSL, first list available devices in PowerShell, then bind and attach the target device.

Lists all connected USB device with their bus IDs:
```bash
usbipd list
```

Binds the specified device:
```bash
usbipd bind --busid [bus ID]
```

Attaches the bound device to WSL:​
```bash
usbipd attach --wsl --busid [bus ID]
```

## How to execute the project
1. First of all, upload the `person_detector_project.ino` sketch to your Arduino board using the Arduino IDE.
2. **Device Permissions (Linux/WSL)**
Grant user permissions to the serial device:
```bash
sudo chown $USER /dev/tty*
```
Replace * with your Arduino port (e.g., /dev/ttyUSB0 or /dev/ttyACM0).

3. **Build the Package**
Navigate to your workspace root and build:
```bash
colcon build --merge-install --symlink-install
```
4. **Source the Workspace**
```bash
source install/setup.bash
```
5. **Run the nodes**
Open separate terminals (keep sourcing `install/setup.bash` in each) and launch:
```bash
ros2 run MMI_Project_Package cam_reader
```
```bash
ros2 run MMI_Project_Package user_position_detector
```
```bash
ros2 run MMI_Project_Package microcontroller_communicator
```
6. **Monitor Data**
```bash
ros2 topic echo /user_position_code
```

## Final Result of the Project

https://github.com/user-attachments/assets/e712f173-1c91-433b-b0fd-a491904cb0bd





