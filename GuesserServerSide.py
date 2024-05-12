from flask import Flask
import socket
import math
import random
import json


app = Flask(__name__)

hidden = None

tries = 0


#Creating the game
def generate(low, high, ip):
    random.seed()
    global hidden
    global tries

    #Swapping the values if the user entered them in the wrong order
    temp = 0
    if(low > high):
        temp = low
        low = high
        high = temp

    
    tries = round(math.log(high-low+1,2)) #The equation that calculates the minimum tries is not mine
    hidden = random.randint(low, high)#Chosing the random number
    
    app.run(debug=False, host=ip, port=5000)




@app.route("/", methods=["GET"])
def index():
    #Sending the hidden number and number of tries to any user that connects to the server
    return json.dumps({"hidden" : hidden, "tries" : tries})
    





if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    low = int(input("Enter the lowest number: "))
    high = int(input("Enter the highest number: "))
    print(f"[**] Use {ip} as the ip for clients [**] \n Ignore everything under this message\n")
    generate(low, high, ip)
    


