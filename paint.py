def wall_paint(x,y,cover):
    area=x*y
    print(f"bucket_needed={round(area/5)}") 
l=int(input("enter the length of the wall"))
b=int(input("enter the width of the wall"))
wall_paint(l,b,5)
