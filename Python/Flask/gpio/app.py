from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(17,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
msg = "Both LEDs are off."

togg1 = 0
togg2 = 0

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    global msg
    global togg1
    global togg2
    
    if request.method == "POST":
        msg = "Both LEDs are off."

        push1 = "off"
        push2 = "off"

        push1 = request.form.get("submitBtn1")
        push2 = request.form.get("submitBtn2")
        
        if push1 == 'on' and togg1 == 0:
            GPIO.output(17,GPIO.HIGH)
            togg1 = 1
        elif push1 == 'on' and togg1 == 1:
            GPIO.output(17, GPIO.LOW)
            togg1 = 0

        if push2 == 'on' and togg2 == 0:
            GPIO.output(18,GPIO.HIGH)
            togg2 = 1
        elif push2 == 'on' and togg2 == 1:
            GPIO.output(18, GPIO.LOW)
            togg2 = 0
            
        if push1 != 'on' and push2 != 'on':
            GPIO.output(17,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            push1 = "off"
            push2 = "off"

        if togg1 == 1 and togg2 == 1:
            msg = "Both LEDs are on."
        elif togg1 == 1 and togg2 == 0:
            msg = "Blue LED is on and Green LED is off."
        elif togg1 == 0 and togg2 == 1:
            msg = "Green LED is on and Blue LED is off."
        else:
            msg = "Both LEDs are off."

    return render_template("index.html", msg = msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
