bilangan = 18
 
for i in range(2, bilangan): 
    if bilangan % i == 0: 
        print(f"{bilangan} bukan bilangan prima") 
        break 
else: 
    print(f"{bilangan} adalah bilangan prima") 