"""Write a program that plays a game of rock-paper-scissors with the user,
with the program always choosing rock.  Have the program print out both its choice
and the player’s choice, as well as who wins.  Have it insult the player
and make them lose if they enter in an invalid choice. """

#Get the player's choice
choice = input("Choose Rock, Paper, or Scissors: ")

#Print out the choices
print("You chose " + choice + ".")
print("The computer chose Rock.")

#Rock ties with Rock, Paper wins over Rock, and Scissors loses to rock
if choice == 'Rock' or choice == 'rock':
    print("Tie!")
elif choice == 'Paper' or choice == 'paper':
    print("You Win!")
elif choice == 'Scissors' or choice == 'scissors':
    print("You Lose!")
else:
    print("Learn to read! You lose!")
#The 'or's aren't necessary, but are used here to also accept uncapitalized choices
    
