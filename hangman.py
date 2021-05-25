import random
chosen_word=random.choice(['rakam','kamna','karamvir','chetna','geeta','jaipal'])
print(chosen_word)
x=len(chosen_word)
display=[]
for _ in range(x):
    display+="_"
print(display)
live=6
end_of_game=False
while not end_of_game:
    guess=input("guess any letter to save hangman:-").lower()
    for position in range(x):
        if guess==chosen_word[position]:
            display[position]=guess
    if guess not in chosen_word:
        live-=1
        if live==0:
            end_of_game=True
            print("u lose")
    print(display)
    if '_' not in display:
        end_of_game=True
        print("u win")
        break
