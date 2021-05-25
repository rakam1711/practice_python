def divide(v1,v3):
    return(v1/v3)    
def multiply(v1,v3):
    return(v1*v3)
def add(v1,v3):
    return(v1+v3)
def subtract(v1,v3):
    return(v1-v3)
operation={"/":divide,
      "*":multiply,
      "+":add,
      "-":subtract,
      }
def computer():
    for symbol in operation:
        print(symbol)
    should_continue=True
    while should_continue:    
        x=float(input("enter first value:"))
        s=input("enter the operation:")
        y=float(input("enter second value:"))
        f=operation[s]
        answer=f(x,y)
        print(f"result = {answer}")
        if input("type 'y' to continue ,else write 'n' for fresh starting:")=="y":
            s=input("enter the operation:")
            y1=float(input("enter third value:"))
            f=operation[s]
            answer=f(answer,y1)
            print(f"result = {answer}")
            break
        else:
            should_continue=True
            print("thank you")
            
computer()
