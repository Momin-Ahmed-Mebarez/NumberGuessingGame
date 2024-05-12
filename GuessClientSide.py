import random
import requests
import math
import time

answer = {}
ip = ""


def start():
    #Storing the hidden number and the number of tries
    tries = answer["tries"]
    hidden = answer["hidden"]
    
    print(f"You have {tries} tries good luck!")
    
    for i in range(tries):
        guess = int(input("Guess a number: "))
        #A true condation while the user have tries and as long as he didn't guess the right number
        if(i != tries-1 and guess != hidden):
            #Giving hints to the user
            if(guess > hidden):
                print("You guessed higher")
            elif(guess < hidden):
                print("You guessed lower")
        else:
            #A condation to handle running out of guesses
            if(guess != hidden):
                print(f"Sorry you ran out of tries\nThe number was {hidden} ")
                break
            #A condation to handle winning
            else:
                print(f"Wow you did it in {i + 1} tries")
                break
    return









if __name__ == "__main__":
    #Asking the user to enter the ip he wants to conncet to
    ip = input("Enter the server ip: ")
    ip = "http://" + ip + ":5000/"

    #Getting the server response (The hidden number and the number of tries) as json 
    answer = requests.get(ip)
    answer = answer.json()
    start()
    time.sleep(60) # Giving the user time to see the reasult
    
