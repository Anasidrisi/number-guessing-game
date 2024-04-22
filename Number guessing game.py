import random
l = [ "rock", "scissor","paper"]   







while True:
    ccount=0
    ucount=0
    uc = int(input('''
game start....                  
1 Yes                  
2 No | exit                  
               '''))
    
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rock
2 Scissor
3 Paper                                
                                
                                
                                
                                '''))
            
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("User value",Cchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice==
                 "paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("You win")
                ucount=ucount+1
                ccount=ccount+1  
            else:
                print("Computer value",Cchoice)
                print("User value",Cchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
                
        if ucount==ccount:
            print("Final game draw...")
            print("User Score", ucount)
            print("Computer Score",  ccount) 
        elif ucount>ccount:
            print("Final you win the game...")
            print("User Score", ucount)
            print("Computer Score",  ccount)
        else:
            print("Computer win the game...")
            print("User Score", ucount)
            print("Computer Score",  ccount)    
                       
                
                                                                       
    else:
        break
    