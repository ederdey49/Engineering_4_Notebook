from flask import Flask, render_template, request #we're importing more elements of flask this time
import RPi.GPIO as GPIO #and the GPIO object from this library

GPIO.setwarnings(False) #this turns off some annoying error messages
GPIO.setmode(GPIO.BCM) #this tells the code to use the T-cobbler's numbering for GPIO pins, not the Pi's
GPIO.setup(17,GPIO.OUT) #set pin 17 to output
GPIO.setup(18,GPIO.OUT) #set pin 18 to output

GPIO.output(17,GPIO.LOW) #turn pin 17 off
GPIO.output(18,GPIO.LOW) #turn pin 18 off
msg = "Both LEDs are off." #make msg read this

togg1 = 0 #these are used to store whether or not the LEDs are on
togg2 = 0

app = Flask(__name__) #new flask app

@app.route("/", methods=["GET","POST"]) #there are two methods at the root directory
def index(): #here's the function to run
    global msg #these variables are defined as global so they can be accessed and modified both within and outside the function
    global togg1
    global togg2
    
    if request.method == "POST": #if the HTML file runs the POST method, which it will do every time a button is clicked
        msg = "Both LEDs are off."

        push1 = "off" #set these to 'off' by default
        push2 = "off"

        push1 = request.form.get("submitBtn1") #change the values to what the website's buttons say when they are pushed
        push2 = request.form.get("submitBtn2")
        
        if push1 == 'on' and togg1 == 0: #if button 1 gets pushed while the LED is off
            GPIO.output(17,GPIO.HIGH) #turn the LED at pin 17 on
            togg1 = 1
        elif push1 == 'on' and togg1 == 1: #if button 1 gets pushed while the LED is on
            GPIO.output(17, GPIO.LOW) #turn pin 17 off
            togg1 = 0

        if push2 == 'on' and togg2 == 0: #if button 2 gets pushed while the LED is off
            GPIO.output(18,GPIO.HIGH) #turn pin 17 on
            togg2 = 1
        elif push2 == 'on' and togg2 == 1: #if button 2 gets pushed again while the LED is on
            GPIO.output(18, GPIO.LOW) #turn pin 17 off
            togg2 = 0
            
        if push1 != 'on' and push2 != 'on': #if neither buttons have been pushed yet
            GPIO.output(17,GPIO.LOW) #turn both pins off
            GPIO.output(18,GPIO.LOW)
            push1 = "off" #tell the program the buttons have not been pushed
            push2 = "off"

        if togg1 == 1 and togg2 == 1: #if both LEDs are on
            msg = "Both LEDs are on."
        elif togg1 == 1 and togg2 == 0: #if only the blue LED is on
            msg = "Blue LED is on and Green LED is off."
        elif togg1 == 0 and togg2 == 1: #if only the green LED is on
            msg = "Green LED is on and Blue LED is off."
        else: #if both LEDs are off
            msg = "Both LEDs are off."

    return render_template("index.html", msg = msg) #give this information to the HTML file

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80) #run the app so it can be accessed on other computers
    
#this app file interacts with the HTML file to make a working website
