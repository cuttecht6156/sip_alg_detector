import socket
from datetime import datetime

#   Build SIP socket
sipsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sipsocket.bind(("",5060))
sipsocket.listen(5)
logmessage = "----ACTIVITY LOG----"

#   Build function for logging past messages
def log():
#   Create variable for current time
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    dt = "\nMessage Received: " + dt_string + "\n"
#   Create variable for connected IP
    fromip = "From IP address: " + address[0] + "\n"
#   Open file and write message from client
    logfile = open("log.txt", "a")
    logfile.write(logmessage + dt + fromip + testresult + response + "\n\n")
    logfile.close()

#   Wait for connections and relay messages once received
while True:
#   Accept incoming connection
    connection, address = sipsocket.accept()
    response = connection.recv(1024).decode("utf-8")
    #print(response)
    connection.send(response.encode("utf-8"))
#   Receive/print test result and write log file
    testresult = connection.recv(1024).decode("utf-8")
    log()
    print(testresult)
    print("Test with " + address[0] + " complete and logged to log.txt")
    break