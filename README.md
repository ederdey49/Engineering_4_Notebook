## Engineering 4 Notebook
by Ned and Lucia

## Table of Contents
[Hello World Generator](#hello-raspberry-pi-zero)

[Six-Sided Number Cube Roller](#dice-roller)

[Somehow So Much Worse Than Just a Regular Calculator](#calculator)

[Fancy Quadratic Calculator](#quadratic-solver)

[Loop De Loop](#strings-and-loops)

[The Death Penalty](#msp)

[LED Blink But Make It Fancy](#gpio-pins-bash)

[LED Blink But Make It Fancier](#gpio-pins-python)

[Using Phones In Class Is Legal Now?](#gpio-pins-ssh)

[LED Blink But Make It Phones](#gpio-pins-flask)

[Instagram](#pi-camera)

[You Wouldn't Download A Car](#hack-your-stuff)

[I Sadly Could Not Come Up With A Good Name For This One](#copypasta-parent-detector)

[1500 Years Of Downloading Libraries](#copypasta-stop-motion)

### Hello Raspberry Pi Zero
#### Objectives
For this assignment, we had to set up our Raspberry Pi and code it to make the Pi print "Hello World!" ten times- code found [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Scripts/LED_Blink.sh).

#### Lessons Learned
During this assignment, we learned some basics in Bash and how the Pi terminal works, as well as how to set up the Pi and attach it to the monitor. 

### Dice Roller
#### Objectives
The objective of this assignment was to make a little program that, when the user presses enter, displays a random number between 1 and 6, like a dice roll. Code found [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/DiceRoller.py).

#### Lessons Learned
From this assignment, we learned some basics of how Python works, because in previous years we'd coded in C, and if you've taken AP Computer Science (like me), then you learn Java, so Python is new. 

### Calculator
#### Objectives
The objective of this assignment was to get the pi to run 5 operations on numbers input by the user- addition, subtraction, multiplication, division, and modulo- and then return all of those results. Code found [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Calculator.py).

#### Lessons Learned
We learned more about how Python works, and more specifically about how functions work in Python, as well as the types of variables. 

### Quadratic Solver
#### Objectives
The objective of this assignment was to solve for the roots of a quadratic function filled in by the user. The difficulty comes from the fact that the program has to first figure out how many roots the quadratic has. Code is [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/QuadSolver.py).

#### Lessons Learned
We learned more about Python and how variables work in Python. 

### Strings and Loops
#### Objectives
The objective of this assignment was to take a string input by the user and return it as each letter separately.
#### Lessons Learned
We learned how to use the String.split() function, which turns a string into a list of words. We also learned how flexible Python is with variables and types, as we could easily treat an element of the word list its own list of letters. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/WordSplitter.py).

### MSP
#### Objectives
This project was a bit bigger than the others. We had to make a fully-functioning game of hangman in which one player enters a phrase, the other player guesses letters, and the computer draws the hangman (or man-shaped piñata, I guess), guessed letters, and blanks thus far.
#### Lessons Learned
We learned how to break a complex piece of code into multiple more manageable methods that can be called throughout the program. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/MSP.py).

### GPIO Pins Bash
#### Objectives
Write a program that takes advantage of the Pi's GPIO (general purpose input/output) pins to turn LEDs on and off in a blinking pattern.
#### Wiring
We just hooked a couple LEDs up to the T-Cobbler.
#### Lessons Learned
We learned how to write a Bash script that can activate and deactivate GPIO pins. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Scripts/LED_Blink.sh).

### GPIO Pins Python
#### Objectives
We did the same thing we did in the last project, but in Python this time.
#### Lessons Learned
We learned that, unlike in Bash, there is no built-in compatibility with GPIO. We had to use a GPIO library, which had completely different syntax to the Bash program. Now we can do stuff with GPIO in Python and take advantage of out T-Cobbler to do it. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/LED_Blink.py).

### GPIO Pins SSH
#### Objectives
All we had to do for this one was use a phone to send information to the Pi to turn GPIO pins on and off.
#### Lessons Learned
We learned how to use an SSH app to connect to our Pi's IP address over Wifi. We used Bash commands to turn the lights on and off, and even ran the Python script from the last project remotely.

### Hello Flask
#### Objectives
We learned to use Flask, which lets us host a webpage on our Pi's IP address that can be accessed by other computers.
#### Lessons Learned
We learned how to use Flask to create a really basic webpage (it literally just says "hello world!"). Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Flask/hello_world/app.py).

### GPIO Pins Flask
#### Objectives
This one was a good bit harder. We made a webpage with two buttons that could actually turn the LEDs on and off and tell the user which are on by communicating with the Pi. We needed both a Python script and an HTML file.
#### Lessons Learned
We learned a lot of HTML and CSS and got more familiar with Flask, which is really hard to use. We learned how to send information back and forth between the Python script and the HTML file through the webpage. Python code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Flask/gpio/app.py) and HTML code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Flask/gpio/templates/index.html).

### GPIO Pins I2C
#### Objectives
We had to use an accelerometer to take measurements and a small LCD screen to display the directional components of acceleration.
#### Wiring
We hooked the accelerometer and the LCD up to the T-Cobbler.
#### Lessons Learned
We learned some of the syntax for creating a display image on an LCD screen, and how to read the data from the accelerometer into the Pi. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/GPIO%20Pins-%20I2C.py).

### Headless
#### Objectives
For this one, we just had to do make the same setup wireless, and draw a graph of one component of acceleration on the LCD.
#### Wiring
We added a battery through the Pi's battery power port.
#### Lessons Learned
We learned how to power a Pi through a battery (we needed some special parts) and how to draw shapes on the LCD. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Headless.py).

### Pi Camera
#### Objectives
We wrote three Python scripts to explore the functions of the Pi Camera. The first just opens a preview for five seconds and closes it. The second loops through all the camera's effects and takes photos with the first five in effect. The third records a ten-second video.
#### Wiring
We plugged the camera into the Pi.
#### Lessons Learned
We learned a lot of syntax for making the camera work. Now we can take pictures and videos and stuff. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/camera_test01.py) and [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/camera_test02.py) and [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/camera_test03.py). Photos and videos [here](https://github.com/lcrosby13/Engineering_4_Notebook/tree/master/Python/Photos).

### Hack Your Stuff
#### Objectives
In this colorfully named assignment, we had to ruin a perfectly good door alarm so we could activate it with our Pi. The noise was extremely annoying.
#### Wiring
We hooked up the doorbell and an SPDT switch to the T-Cobbler. Because the GPIO pins only output 1 volt, the alarm didn't really work, so we ran its power line through a transistor.
#### Lessons Learned
We got some practice with reading GPIO pins in Python. We learned that we can use the Pi to add more complex functionality to basically anything that takes power. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/HackYourStuff.py).

### Copypasta Parent Detector
#### Objectives
We had to make a PIR (passive infrared) motion sensor trigger the Pi camera to take a ten-second video and save it with a date and time stamp.
#### Wiring
We plugged the camera into the Pi and hooker the PIR sensor up into the T-Cobbler.
#### Lessons Learned
We learned how to use a PIR sensor, and how to use Pyhton's datetime library to return the current date and time. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Copypasta%20Parent%20Trap.py) and videos [here](https://github.com/lcrosby13/Engineering_4_Notebook/tree/master/Python/Photos).

### Copypasta Stop Motion
#### Objectives
We had to use the Pi camera to make a stop-motion video by taking photos and compiling them. Each time a button was pushed, we saved it with a number to keep the frames in order, and after we took all the photos, we used ffmpeg to make a video.
#### Wiring
We plugged the camera into the Pi and hooked up a push button to the T-Cobbler.
#### Lessons Learned
We learned that downloading and installing a program on the Pi takes approximately 1500 years on CHS wifi. Also, ffmpeg isn't very good at compiling videos; the framerate was never what we actually set it to, and if we just set it too low, the video wouldn't play right. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Copypasta%20Stop%20Motion.py), frames and videos [here](https://github.com/lcrosby13/Engineering_4_Notebook/tree/master/Python/Animation).
