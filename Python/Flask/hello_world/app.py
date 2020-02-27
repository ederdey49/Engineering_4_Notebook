from flask import Flask #import the Flask object from the flask directory

app = Flask(__name__) #make a Flask object called app

@app.route("/") #at the root directory,
def hello_world(): #this is the function to be run
	return "hello world!" #all it does is print this text

if __name__ == "__main__":
	app.run(host= "0.0.0.0", port = 80) #run the app so it's visible to outside computers
	
#this script creates a webpage that you can visit at the pi's IP address
