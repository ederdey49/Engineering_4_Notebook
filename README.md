## Engineering 4 Notebook
by Ned and Lucia

## Table of Contents
[Hello World Generator](#hello-raspberry-pi-zero)

[Six-Sided Number Cube Roller](#dice-roller)

[Somehow So Much Worse Than Just a Regular Calculator](#calculator)

[Fancy Quadratic Calculator](#quadratic-solver)

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
#### Lessons Learned
We learned some of the syntax for creating a display image on an LCD screen, and how to read the data from the accelerometer into the Pi. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/GPIO%20Pins-%20I2C.py).

### Headless
#### Objectives
For this one, we just had to do make the same setup wireless, and draw a graph of one component of acceleration on the LCD.
#### Lessons Learned
We learned how to power a Pi through a battery (we needed some special parts) and how to draw shapes on the LCD. Code [here](https://github.com/lcrosby13/Engineering_4_Notebook/blob/master/Python/Headless.py).

### Pi Camera
#### Objectives
We wrote three Python scripts to explore the functions of the Pi Camera. The first just opens a preview for five seconds and closes it. The second loops through all the camera's effects and takes photos with the first five in effect.
#### Lessons Learned


### Hack Your Stuff
#### Objectives

#### Lessons Learned

### Copypasta Parent Detector
#### Objectives

#### Lessons Learned

### Copypasta Stop Motion
#### Objectives

#### Lessons Learned
