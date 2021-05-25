alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def comandow(letter,shift):
    x=""
    for i in letter:
        position=alphabet.index(i)
        new_position=position+shift
        x+=alphabet[new_position]
    print(f"encrypted letter is :{x}")
    
    y=""
    for i in x:
        position=alphabet.index(i)
        new_position=position-shift
        y+=alphabet[new_position]
    print(f"decrypted letter is:{y}")   


l=input("enter the letter:").lower()
s=int(input("enter the shift:"))
comandow(l,s)
