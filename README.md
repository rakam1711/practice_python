# practice_python
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','^','&','*','(',')','+']

print('welcome to the password generator')

nr_letter=int(input("how many letter would u like in ur password:\n"))
nr_number=int(input("how many number would u like in ur password:\n"))
nr_symbol=int(input("how many symbol would u like in ur password:\n"))
password=[]
for i in range(1,nr_letter+1):
    password.append(random.choice(letter))
for i in range(1,nr_number+1):
    password+=random.choice(number)
for i in range(1,nr_symbol+1):
    password+=random.choice(symbol)
print(password)
random.shuffle(password)
password1=""
for i in password:
    password1+=i
    
print(f"ur password is:{password1}")
    
