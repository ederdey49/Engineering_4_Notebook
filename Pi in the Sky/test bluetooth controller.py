import bluetooth
import time

while True:
    result = bluetooth.lookup_name("PG-9021", timeout = 50)
    if(result == None):
        print("Not detected")
    else:
        print("found")
    
