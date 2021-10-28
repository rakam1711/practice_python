# practice_python
dict={}
x=int(input('enter the number of students:'))
for _ in range(x):
    name = input('enter the name of the student:')
    score = float(input('enter the score also:'))
    dict[name]=score
min=min(dict.values())
max=max(dict.values())        
for i in sorted(dict.values()):
    if i>min and i<max:
        max=i

keylist=list(dict.keys())

vallist=list(dict.values())

li=[]
for j in range(len(vallist)):
   
    if vallist[j]==max:
        li.append(keylist[j])

li.sort()
for i in li:
    print(i)
