Alpha = "abcdefghijklmnopqrstuvwxyz"
x = 1
while x:
    option = ""
    for i in range(0,26):
        for y in range(0,x):
            option = option + Alpha[i]
    print("")
    print(option)
    x+=1
    if x >3:
        break
