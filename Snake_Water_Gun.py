import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice (s,w,g): ")
choices = {'s':-1, 'w':0, 'g':1}
reverse={-1:"snake", 0:"water", 1:"gun"}
you=choices[youstr]
print("You chose:", reverse[you])
print("Computer chose:", reverse[computer])
if(computer==you):
    print("It's a tie!")
else:
    if((you==1 and computer==-1) or (you==-1 and computer==0) or (you==0 and computer==1)):
        print("You win!")
    elif((computer==1 and you==-1) or (computer==-1 and you==0) or (computer==0 and you==1)):
        print("You lose!")