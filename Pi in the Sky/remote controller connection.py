import bluetooth

target_address = "98:B6:E9:04:4F:B5"

def findDevice(target_name):
    target_address = ""

    nearby_devices = bluetooth.discover_devices(duration=10, flush_cache=True)
    
    for i in nearby_devices:
        print (i)
        if target_name == bluetooth.lookup_name(i):
            target_address = i

    if target_address is not "":
        print ("found target bluetooth device with address ", target_address)
    else:
        print ("could not find target bluetooth device nearby")

    return str(target_address)

def receive(target_name):
    target_address = findDevice(target_name)
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)
    client_sock.address = server_sock.accept()
    print ("Accepted connection from", target_address)
    data = client_sock.recv(1024)
    print ("received [%s]" % data)

    client_sock.close()
    server_sock.close()

def send(target_name):
    bd_addr = str(findDevice(target_name))
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    sock.send("sdfjksdf")
    
    sock.close()

    
#receive("Ned's Samsung")
#send("Pro Controller")

print (bluetooth.discover_devices(duration=20, flush_cache=True, lookup_names=True))
    

