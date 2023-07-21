## Table of contents

* [Project's Title](#"project's-title)
* [Project Description](#project-description)
* [Setup](#setup)
* [How to Use the Project](#How-to-Use-the-Project)
* [Tools](#tools)
* [Hardware](#hardware)
* [For More Information](#for-more-information)
* [Credits](#credits)

## Project's Title
  <p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/DarkMode.png height="400" width="400"></p>
 

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

 <p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110331.png height=400 width=500></p>

  - Second, you will create a new virtual port

 <p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110405.png height=400 width=500></p>

  - Click next

 <p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110433.png height=400 width=500></p>

  - Make sure you choose COM3 for the virtual port

 <p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-11%20110452.png height=400 width=500></p>   

- after making sure you have all the libraries installed, you should be able to run the project without any issues. 

- If you successfuly manage to open the project, you have to login as an admin first with the username 'admin' and password 'admin' to start adding users and use the system
  - Note that the username and password for the admin are customizable for anyone using the system, but for testing purposes and ease of   use, these credintials will remain as it is.      
- Now to simulate and see how the project works in real life, you would need to download Protues software which is used to simulate embedded systems projects. To download Protues <a href=https://drive.google.com/file/d/18dc8n0lpLu9QRzxbgZzciAwhg6NeqnPp/view>Click Here </a>
- After installing Protues, you can go to the 'Protues Design' folder and open up the 'test.pdsprj' file.
- after opening, it should look like this
  
<p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-17%20214411.png height=400 width=700></p>   

- You can now run the simlulation using the button on the bottom left corner
 
<p align='center'> <img src=https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/project/icons/Screenshot%202023-07-17%20214834.png height=400 width=700></p> 

- Now the simulation is running and waiting for some action from the application.
- For more information, check out the demo video <a href= "https://www.youtube.com/watch?v=ity_Aa_V_a8&feature=youtu.be">Here</a>.

## Tools and Technologies

- You can find the dataset used to train the head detection model <a href="https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release" >Here</a>
- We used Roboflow, a website used to train and deploy machine learning models easily, you can check the website <a href="https://roboflow.com/">Here</a>. For more information on how to use the website you can check the video <a href="https://www.youtube.com/watch?v=wuZtUMEiKWY&t=1082s">Here</a>

- Programming language, modules and softwares used
  - Python
  - OpenCV
  - Tkinter
  - SQLite Database
  - Raspbian OS if RPI exists otherwise Windows OS
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
- Please Look [Here](https://github.com/Mostafa-Usama/Smart-Classroom/tree/main/Documents) for full Documentation. 
  - Documents
    - Project proposal
    - The software requirements specifications
    - Software Design Document
    - Implementation plan
    - Test Plan
  - Report
    - part one
    - part two
  - Presentation
    - part one
    - part two
  - [Demo](https://github.com/Mostafa-Usama/Smart-Classroom/blob/main/demo.mp4)

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



