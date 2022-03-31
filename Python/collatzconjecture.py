for i in range (1,500000000000000000):
    value = i
    while value != 1:
        if value%2 == 0:
            value = value/2
        else:
            value = value*3+1
    print("arrived")
