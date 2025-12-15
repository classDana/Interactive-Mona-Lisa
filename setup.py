from setuptools import find_packages, setup

package_name = 'MMI_Project_Package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Daniela Milisic',
    maintainer_email='e12005942@student.tuwien.ac.at',
    description='User tracking ROS2 package',
    license='Apache Licence 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'cam_reader = MMI_Project_Package.cam_reader:main',
            'user_position_detector = MMI_Project_Package.user_position_detector:main',
            'microcontroller_communicator = MMI_Project_Package.microcontroller_communicator:main',
        ],
    },
)
