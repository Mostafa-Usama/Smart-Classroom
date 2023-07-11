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
    
    - The smart classroom system is a new self-contained product which will be produced in order to overcome the problem of wasting energy.
    - The classroom system manages the electrical devices in the classroom by collecting data from sensors and cameras, then processing this data, taking action, and finally sending orders to the lighting system, air conditioning, and more.

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
  - NumPy: `pip install numpy`
  - Ultralytics: `pip install ultralytics`
  - serial: `pip install pyserial`


## How to Use the Project

- First, you need to set up VSPE.
  
  - To do that, you will first open VSPE which will look something like this

<img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110331.png height=400 width=500>

  - Second, you will create a new virtual port

<img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110405.png height=400 width=500>

  - Click next

<img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110433.png height=400 width=500>

  - Make sure you choose COM3 for the virtual port

<img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110452.png height=400 width=500>   

- after making sure you have all the libraries installed, you should be able to run the project without any issues. 

- If you successfuly manage to open the project, you have to login as an admin first with the username 'admin' and password 'admin' to start adding users and use the system
  - Note that the username and password for the admin are customizable for anyone using the system, but for testing purposes and ease of   use, these credintials will remain as it is.      

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



