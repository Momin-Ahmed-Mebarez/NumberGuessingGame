import random
import math

def start(lowest, highest):
    hidden = random.randint(lowest, highest)
    #Deciding the number of tries based on the range of numbers
    tries = round(math.log(highest-lowest+1,2)) #The equation that calculates the minimum tries is not mine
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


#Swapping the values if the user entered them in the wrong order
def valdiate(lowest, highest):
    temp = 0
    if(lowest > highest):
        #A simple swapping aloghartim 
        temp = lowest
        lowest = highest
        highest = temp
        start(lowest, highest)
    else: start(lowest,highest)










if __name__ == "__main__":
    lowest = int(input("Enter the lowest number: "))
    highest = int(input("Enter the highest number: "))
    valdiate(lowest,highest)
