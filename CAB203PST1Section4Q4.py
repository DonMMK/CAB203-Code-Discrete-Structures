def myfunction():
    MyFirstSet = []
    MySecondSet = []
    MyFirstSet = [5 * 2, 6 * 2, 7 * 2]

    for i in range(-60, 61):
        if i != 0 and 60 % i == 0:
            MySecondSet.append(i)
            Final = list(set(MyFirstSet) & set(MySecondSet))
            print(Final)
            
	
