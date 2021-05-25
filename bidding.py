
def winner():
    top=0
    for i in bid:
        if bid[i]>=top:
            top=bid[i]
    print(f"the winner of this bid is {i}\n  with bidding price:{top}")
bid={}
not_bidding=False
while not not_bidding:
    name=input("enter ur name:")
    bidding=int(input("enter the amount of bidding:"))
    bid[name]=bidding
    x=input(" type 'yes' if u want more bidding else type 'no'")
    if x=="no":
        not_bidding=True
        winner()
    elif x=="yes":
        print("                                                          \n                                                    \n\n\n\n\n\n\n\n\n\n\n")    
        

