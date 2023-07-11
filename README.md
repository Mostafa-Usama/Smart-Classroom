## Table of contents

* [Project's Title](#Project's-Title)
* [Project Description](#Project-Description)
* [Setup](#setup)
* [How to Use the Project](#How-to-Use-the-Project)
* [Tools](#Tools)
* [Hardware Component](#Hardware-Component)
* [For More Information](#For-More-Information)
* [Credits](#Credits)

## Project's Title
Smart Classroom
<img src=https://github.com/Mohamed-Nabi1/Smart-Classroom/assets/124218766/844b657d-385e-4324-bbe1-89ee8b7e6785 align="center" height="400" width="500">
## Project Description
  - Overview
    
    - The smart classroom system is a new product that manages electrical devices in the 
    classroom by collecting and processing data from sensors and cameras to control  
    lighting, air conditioning, and more. The system aims to increase efficiency and reduce 
    energy waste.
    As previously mentioned, this system works to reduce energy consumption through 
    various processes. This will be achieved through some of its features, such as 
    automatic operation. The system will automatically turn on and off at the scheduled 
    start and end times of lectures each week, without human intervention.

  - Features of the project
    
    - Create a study schedule that will make the system operate automatically at the start of 
    each lecture and stop at its end, achieving the desired goal of the system, which is to conserve energy.
    - Count the number of people in a specific section of the classroom.
    - Control the lighting in a specific space based on the number of people in that space and turn it off when not in use.
    - Control air conditioners in a specific place based on the temperature and the 
    number of people present in that place and shut them down when not in use.

  - Architecture
    
    - Sensors: Measures the temperature of its environment and converts the input data into
    electronic data to record then send this data to Raspberry PI
    - Cameras: Iteratively collect images and send these images to Raspberry PI
    - Raspberry PI: The photos taken from the cameras and temperature read from sensors are 
    analyzed and passed through the system to count the number of students, find out their locations, 
    perform some operations, then decide whether to turn on the devices or not and send the 
    command taken to the electrical devices.
    - Electrical Devices: Through commands sent to the devices, the devices are turned on or off
      
## Setup

- install VSPE
- install proteus
- install SQLite
- install these libraries
  - OpenCV: `pip install opencv-python`
  - Tkinter: Tkinter is a built-in Python library, so you don't need to install it separately.
  - NumPy: `pip install numpy`
  - Ultralytics: `pip install ultralytics`
  

Once you have installed these libraries and programs, you should be able to run the project without any issues.

## How to Use the Project

## Tools

- SQLite Database
- Raspbian OS if RPI exists otherwise Windows OS
- OpenCV
- Python
- Tkinter
- YOLOv8
- NumPy
- Proteus

## Hardware

- Heat sensors: These sensors are used to measure the temperature of the classroom.
- Camera: This is used to count the number of people in the classroom.
- Raspberry Pi microprocessor: This is the brains of the system. It collects data from the sensors, processes it, and sends commands to the electrical devices.
- Screwdriver: This is used to install the hardware components of the system.
- Wiring and Cables: This is used to connect the hardware components of the system.
- Power supply: This is used to power the system.
- Electrical outlets: This is where the system will be plugged in.


## For More Information
@ Please Look [Here](https://github.com/Mohamed-Nabi1/Smart-Classroom/tree/main/Documents)
- Documents
  - project proposal
  - the software requirements specifications
  - Software Design Document
  - implementation plan
  - Test Plan
- Report
  - part one
  - part two
- Presentation
  - part one
  - part two
- [Demo](https://github.com/Mohamed-Nabi1/Smart-Classroom/blob/main/demo.mp4)

## Credits
- Team Members
  - Mohamed Nabil ([GitHub](https://github.com/Mohamed-Nabi1)) ([LinkedIn](https://www.linkedin.com/in/mohamed-nabil-hassan/))
  - Mostafa Usama  ([GitHub](https://github.com/Mostafa-Usama)) ([LinkedIn](https://www.linkedin.com/in/mostafa-usama/))
  - Mohamed Ramadan ([GitHub](https://github.com/MoohamedRamadan)) ([LinkedIn](https://www.linkedin.com/in/mohamed-ramadan-farouk/))
  - Nourhan Mahmoud ([GitHub](https://github.com/nourrrhan)) ([LinkedIn](https://www.linkedin.com/in/nourrrhan/))
  - Sondos Osama ([GitHub](https://github.com/sondosmm)) ([LinkedIn](https://www.linkedin.com/in/sondos-osama-984486202/))
  - Manar Mohamed ([GitHub](https://github.com/Mannar324)) ([LinkedIn](https://www.linkedin.com/in/mannar-alansary-515334219/))
- Supervisor:
  - Dr. Abdelrahaman Hedar ([LinkedIn](https://www.linkedin.com/in/abdel-rahman-hedar-35528538/))



