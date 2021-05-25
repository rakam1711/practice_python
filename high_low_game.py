data=[{'name':'modi','follower':55,'description':'politician'},
      {'name':'ronaldo','follower':100,'description':'football player'},
      {'name':'akshay kumar','follower':50,'description':'bollywood actor'},
      {'name':'salaman','follower':40,'description':'bollywood actor'},
      {'name':'nasa','follower':66,'description':'research centre'},
      {'name':'isro','follower':1,'description':'research centre'},
      {'name':'manoj bajpye','follower':3,'description':'actor'},
      {'name':'jetalal','follower':2,'description':'tv actor'},
      {'name':'parmish verma','follower':6,'description':'singer'},
      {'name':'jassi gill','follower':8,'description':'singer'},
      {'name':'ragnar','follower':4,'description':'viking ka actor'},
      {'name':'dragon girl','follower':27,'description':'holliwood actress'},
      {'name':'who','follower':10,'description':'health centre'},
      {'name':'yogi','follower':2,'description':'politician'},
      {'name':'pankaj tripati','follower':3,'description':'actor'},
      ]
import random
import os

def random_pickup():
    return random.choice(data)
def check(answer_a,answer_b):
    n=(answer_a["name"])
    x=(answer_a['follower']) 
    y=(answer_a["description"])
    print(f"(A):name of the instagramer is {n} and he is an {y}")
    print("VS")
    n1=(answer_b['name'])
    x1=(answer_b['follower']) 
    y1=(answer_b["description"])
    print(f"(B):name of the instagramer is {n1} and he is an {y1}")
    if x>x1:
        return('a')
    else:
        return('b')
def game():
    answer_a=random_pickup()
    answer_b=random_pickup()
    highest_follower=check(answer_a,answer_b)
    s=0
    should_continue=True
    while should_continue:
        answer_a=answer_b
        answer_b=random_pickup()
        
        guess=input("enter your choice from A and B,who has more follower").lower()
        if guess==highest_follower:
            print("u r right")
            s+=1
            print(f"your score is {s}")
            os.system('clear')
            highest_follower=check(answer_a,answer_b)
            should_continue=True
        else:
            print("sorry u r wrong")
            print(f"your final score is {s}")
            should_continue=False
            
    
game()
