import random

stone='''STONE(0) '''
paper=''' PAPER(1) '''
sissor='''SISSIR(2) '''
print(stone,paper,sissor)

user_choice=int(input(" press 0 for stone: \n press 1 for paper: \n press 2 for sissor:\n=>"))

pc_choice=random.randint(0,2)
print(f"computer choose: {pc_choice}")
if user_choice==0 and pc_choice==2:
    print("you wins")
elif user_choice==1 and pc_choice==0:
    print("you win")
elif user_choice==2 and pc_choice==1:
    print(" you win")
elif user_choice==0 and pc_choice==1:
    print("u lose")
elif user_choice==1 and pc_choice==2:
    print("u lose")
elif user_choice==2 and pc_choice==0:
    print("u lose")
else:
    print("match draw")
    



