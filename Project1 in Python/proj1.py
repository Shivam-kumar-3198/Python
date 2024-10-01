# # # We all have played snake, water gun game in our childhood.If you haven't google the rules and
# # write the python code capable of playing by user 
# write the code for it 
computer = -1
youstr = input("Enter Your Choice here : ")
youDict = {"s":1, "w":-1, "g":0 }
you = youDict[youstr]

if(computer ==-1 and you ==1):
    print("you win!!")

elif(computer ==-1 and you ==0):
    print("You Lost!")

if(computer ==1 and you ==-1):
    print("You Lose!")

elif(computer ==1 and you == 0):
    print("You Win!!") 

if(computer ==0 and you ==-1):
    print("You Win!")

elif(computer ==0 and you ==1):
    print("You Lose!!") 
    
      

