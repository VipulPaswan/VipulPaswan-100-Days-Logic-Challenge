li = [20,40,30,56,60,50,80,90]
it = iter(li)


while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
    
    
#---- OUTPUT ---- 
20
40
40
30
56
60
50
80
90

