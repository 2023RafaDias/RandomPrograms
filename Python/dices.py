Alpha = "abcdefghijklmnopqrstuvwxyz"
x = 1
for i in range(0,x):
    print(26**x)
    for i in range(26**x,0,-1):
        remainders = []
        number = i
        while number > 0:
            remainders.append(number%26)
            number = int((number-(number%26))/26)


        for i in range(len(remainders)-1,-1,-1):
                print(Alpha[remainders[i]-1])

