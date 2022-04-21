import socket
import filecmp
import tkinter as tk
from tkinter import ttk

#   Build function for getting the template file
def getfile():
    getmessage = open("message.txt", "rb")
    message = getmessage.read()
    getmessage.close()
    return message
message = getfile()
#   Build function for running the test
def runtest():
    host = "ec2-52-71-116-190.compute-1.amazonaws.com"
    port = 5060
    sipsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sipsocket.connect((host,port))
    sipsocket.send(message)
    response = sipsocket.recv(1024)
    #   Write response file with data from server
    responsefile = open("response.txt", "wb")
    responsefile.write(response)
    responsefile.close()
    #   Compare files
    messagefile=("message.txt")
    responselog=("response.txt")
    comp = filecmp.cmp(messagefile, responselog, shallow = False)
    #   If files match, send pass to server, if files differ, send fail to server
    if comp == True:
        sipsocket.send("****ALG NOT DETECTED****\n".encode("utf-8"))
        print("****ALG NOT DETECTED****")
        l = tk.Label(b, text="Result: Pass", fg="green").grid(column=0, row=2)
    elif comp == False:
        sipsocket.send("****ALG DETECTED****\n".encode("utf-8"))
        print("****ALG DETECTED****")
        l = tk.Label(b, text="Result: Fail", fg="red").grid(column=0, row=2)
    else:
        l = tk.Label(b, text="Result: ").grid(column=1, row=2)

root = tk.Tk()
root.title("SIP ALG TEST")
root.configure(background="#F0F0F0")
root.geometry("300x150")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=0)
mainframe.rowconfigure(0, weight=0)
t = ttk.Label(mainframe, text="A Simple SIP ALG Test", padding=10).grid(column=0, row=1)
b = ttk.Button(mainframe, text="Run Test", command=runtest, padding=20).grid(column=0, row=2)
root.mainloop()