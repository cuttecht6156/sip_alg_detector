import socket
import filecmp

#   Build function for getting th template file
def getfile():
    getmessage = open("message.txt", "rb")
    message = getmessage.read()
    getmessage.close()
    return message

#   Set message variable equal to data from template file
message = getfile()

#   Connect to server
sipsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sipsocket.connect((socket.gethostname(), 5060))
sipsocket.send(message)
#print(response.decode("utf-8"))

#   Write response file with data from server
response = sipsocket.recv(1024)
responsefile = open("response.txt", "wb")
responsefile.write(response)
responsefile.close()

#   Create variables for files to compare later
messagefile = "message.txt"
responselog = "response.txt"

#   Compare files
comp = filecmp.cmp(messagefile, responselog, shallow = False)
#   If files match, send pass to server, if files differ, send fail to server
if comp == True:
    sipsocket.send("****ALG NOT DETECTED****\n".encode("utf-8"))
    print("****ALG NOT DETECTED****")
elif comp == False:
    sipsocket.send("****ALG DETECTED****\n".encode("utf-8"))
    print("****ALG DETECTED****")