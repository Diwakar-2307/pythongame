import random
Gchoice =["ROCK","PAPER","Scissor"]
while True:
    print(" If both(computer & user ) have same input then match is draw ,"
          " if user have ROCK : then WIN(WHEN PAPER) LOSE:(SCISSOR) \n "
          "if user have PAPER : then WIN(WHEN SCISSOR) LOSE:(ROCK)"
          "\n if user have SCISSOR : then WIN(WHEN ROCK) LOSE:(PAPER) "
          "and vice versa . ")
    print("ROCK PAPER Scissor Game")
    personwin,computerwin=0,0
    for i in range(1,6):
        print("Round", i,"Start : ")
        print("1. ROCK","2. PAPER","3. Scissor", sep="\n")
        print("please select one option ")
        personchoice =int(input())
        if personchoice==1:
            print("You selected Rock")
            personchoice="ROCK"
        elif personchoice==2:
            print("You selected Paper")
            personchoice="PAPER"
        elif personchoice==3:
            print("You selected Scissor")
            personchoice="Scissor"
        else:
            print("Invalid choice")
            break
        computerchoice=random.choice(Gchoice)
        print("Computer select :",computerchoice)

        if personchoice==computerchoice:
            personwin+=1
            computerwin+=1
            print("Round Draw : ")
        elif(personchoice=="PAPER" and computerchoice== "ROCK")or (personchoice=="ROCK" and computerchoice== "Scissor") or (personchoice=="Scissor" and computerchoice== "PAPER"):
            personwin+=1
            print("You win this round")
        else:
            computerwin+=1
            print("Computer win this round")

            # who win the game
    if personwin>computerwin:
                print("Person win the match")
                print("Score of person: ", personwin,"Score of computer: " ,computerwin , sep=" ")
    elif computerwin>personwin:
                print("Computer win the match")
                print("Score of person: ", personwin, "Score of computer: ", computerwin , sep=" ")
    else:
                print ("Match Draw")
                print("Score of person: ", personwin, "Score of computer: ", computerwin , sep=" ")

    Player_choice=input("Want to play again?(YES or NO).").upper()
    if Player_choice == 'YES':
        continue


    else:
        break
