import random
import time
rounds = (1)#the round variable is created
Total_Score1 = (0)#player1's total score is created as a variable
Total_Score2 = (0)#player2's total score is created as a variable


print("-----Dice Rolling Game-----")

print("...HIGHSCORES...")
f = open("highscore.txt","r")#the code opens the highscore.txt for reading only
print(f.read())#the code prints out the highscores
f.close()#the code closes the file


player1_name = input("Enter a name, player 1")#the code asks player 1 to enter a name
while len(player1_name) < 4 or len(player1_name) > 12:#the code checks if the input is valid
    print("Name is invalid")#the code tells the user the name is invalid
    player1_name = input("Enter a name, player 1")
    
player2_name = input("Enter a name, player 2")#the code asks player 2 to enter a name
while len(player2_name) < 4 or len(player2_name) > 12:#the code checks if it is valid
    print("Name is invalid")
    player2_name = input("Enter a name, player 2")
    
time.sleep(1)
while rounds < 6:#the code checks that there has been no more than 5 rounds
    print("---- Round", rounds, "----")#the code prints out what round it is
    print("")
    print("",player1_name,"'s turn")#the code tells player1 it is their go
    time.sleep(1)#the code pauses for one second
    print("")
    roll_die = input("Press 'F' to roll the dice")
    while roll_die != "F":
        print("Waiting...")
        roll_die = input("Press 'F' to roll the dice")
    Die1 = random.randint(1,6)#a random number is generated called Die1
    Die2 = random.randint(1,6)#a random number is generated called Die2
    print(Die1)
    print(Die2)
    time.sleep(1.75)
    Rnd_Total = Die1 + Die2
    if (Rnd_Total)%(2) == 0:#the code checks if the total for the round is even
        if Die1 == Die2:#the code checks if die1 = die2
            Die3 = random.randint(1,6)#a third random number is created
            print("You rolled a double!")
            time.sleep(1)
            print(Die3)#the code prints the third die's value
            Rnd_Total = Rnd_Total + Die3
            Rnd_Total = Rnd_Total + 10
            Total_Score1 = Total_Score1 + Rnd_Total
            Rnd_Total = 0
            time.sleep(1)
            print("",player1_name, "'s total score is now", Total_Score1)#the code prints player1's total score
            print("")
            print("")
            time.sleep(1.5)
        elif Die1 != Die2:
            Rnd_Total = Rnd_Total + 10
            Total_Score1 = Total_Score1 + Rnd_Total
            Rnd_Total = 0
            print("",player1_name, "'s total score is now", Total_Score1)#the code tells player 1 what their total score is
            print("")
            print("")
            time.sleep(1.5)
    elif (Rnd_Total)%(2) == 1:#code checks if total of round is odd
        Rnd_Total = Rnd_Total - 5
        if Rnd_Total >= 0:#code checks if total of round is greater or equal to 0
            Total_Score1 = Total_Score1 + Rnd_Total
            Rnd_Total = 0
            print("",player1_name, "'s total score is now", Total_Score1)
            print("")
            print("")
            time.sleep(1.5)
        elif Rnd_Total < 0:#code checks if total of round is less than 0
            Rnd_Total = 0
            print("",player1_name, "'s total score is now", Total_Score1)
            print("")
            print("")
            time.sleep(1.5)   
    print("", player2_name, "'s turn")#the code displays that it is player 2's turn
    print("")
    time.sleep(1)
    roll_die = input("Press 'F' to roll the dice")
    while roll_die != "F":
        print("Waiting...")
        roll_die = input("Press 'F' to roll the dice")
    Die1 = random.randint(1,6)#a random number is generated called Die1
    Die2 = random.randint(1,6)#a random number is generated called Die2
    print(Die1)
    print(Die2)
    time.sleep(1.75)
    Rnd_Total = Die1 + Die2
    if (Rnd_Total)%(2) == 0:#the code checks if the total for the round is even
        if Die1 == Die2:#the code checks if die1 = die2
            Die3 = random.randint(1,6)#a third random number is created
            print("You rolled a double!")
            time.sleep(1)
            print(Die3)#the code prints the third die's value
            Rnd_Total = Rnd_Total + Die3
            Rnd_Total = Rnd_Total + 10
            Total_Score2 = Total_Score2 + Rnd_Total#the code adds the round total to the total score
            Rnd_Total = 0
            time.sleep(1)
            print("",player2_name, "'s total score is now", Total_Score2)#the code prints player1's total score
            print("")
            print("")
            rounds = rounds + 1#the code adds one to the variable 'rounds'
            time.sleep(1.75)
        elif Die1 != Die2:
            Rnd_Total = Rnd_Total + 10
            Total_Score2 = Total_Score2 + Rnd_Total#the code adds the round total to the total score
            + Rnd_Total
            Rnd_Total = 0
            print("",player2_name, "'s total score is now", Total_Score2)#the code tells player 1 what their total score is
            print("")
            print("")
            rounds = rounds + 1
            time.sleep(1.75)         
    elif (Rnd_Total)%(2) == 1: #code checks if total of round is odd
        Rnd_Total = Rnd_Total - 5
        if Rnd_Total >= 0:#code checks if total of round is greater or equal to 0
            Total_Score2 = Total_Score2 + Rnd_Total
            Rnd_Total = 0
            print("",player2_name, "'s total score is now", Total_Score2)
            print("")
            rounds = rounds + 1
            time.sleep(1.75)
        elif Rnd_Total < 0:#code checks if total of round is less than 0
            Rnd_Total = 0
            print("",player2_name, "'s total score is now", Total_Score2)
            print("")
            rounds = rounds + 1
            time.sleep(1.75)
        

if Total_Score1 == Total_Score2:#the code checks if P1's total score is equal to P2's score
    print("Both players have tied")
    time.sleep(1)
    TieRoll_P1 = random.randint(1,6)
    TieRoll_P2 = random.randint(1,6)
    print("",player1_name,"rolled a" ,TieRoll_P1)
    Total_Score1 = Total_Score1 + TieRoll_P1
    time.sleep(0.5)
    print("",player2_name,"rolled a" ,TieRoll_P1)
    Total_Score2 = Total_Score2 + TieRoll_P2
    time.sleep(0.5)
    while Total_Score1 == Total_Score2 :#the code checks if player1's die is equal to player2's
        TieRoll_P1 = random.randint(1,6)
        TieRoll_P2 = random.randint(1,6)
        print("",player1_name,"rolled a" ,TieRoll_P1)
        Total_Score1 = Total_Score1 + TieRoll_P1
        time.sleep(0.5)
        print("",player2_name,"rolled a" ,TieRoll_P1)
        Total_Score2 = Total_Score2 + TieRoll_P2
        time.sleep(0.5)
        if Total_Score1 > Total_Score2:#the code checks if player1's die rolled greater than player2's
            print("",player1_name, "is the winner")
            f = open("highscore.txt","a")#the code appends to the highscore text file
            f.write("\n")
            f.write(player1_name)#the code prints player1's nam e
            f.write("--")
            f.write(str(Total_Score1))
            f.close()#the code closes the highscore text file
        elif Total_Score1 < Total_Score2:#the code checks if player2's die rolled greater than player1's
            print("",player2_name, "is the winner")
            f = open("highscore.txt","a")#the code appends to the highscore text file
            f.write("\n")
            f.write(player2_name)
            f.write("--")
            f.write(str(Total_Score2))
            f.close()#the code closes the highscore text file
if Total_Score1 > Total_Score2:#the code checks if P1's total score is greater than P2's score
    print("",player1_name, "is the winner")
    f = open("highscore.txt","a")#the code appends to the highscore text file
    f.write("\n")
    f.write(player1_name)
    f.write("--")
    f.write(str(Total_Score1))
    f.close()#the code closes the highscore text file
elif Total_Score1 < Total_Score2:#the code checks if P2's total score is greater than P1's score
    print("",player2_name, "is the winner")
    f = open("highscore.txt","a")
    f.write("\n")
    f.write(player2_name)
    f.write("--")
    f.write(str(Total_Score2))
    f.close()
    
 input("Press any key to exit:")
    



