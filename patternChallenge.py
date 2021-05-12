again = ""
while again != "n":
    error = "yes"
    while error == "yes":
        try:
            size = int(input("What will be the width of your grid? "))
            error = "no"
        except ValueError:
            print("Integer Only!")
        try:
            size2 = int(input("What will be the height of your grid? "))
            error = "no"
        except ValueError:
            print("Integer Only!")
            
    array = []
    for i in range(0,size2):
        array.append([])
        for i in range(0,size):
            array[len(array)-1].append(0)

    for i in range(0,size2):
        for ii in range(0,size):
            if i-1 >= 0:
                array[i][ii] += 1
            if i+1 < size2:
                array[i][ii] += 1
            if ii-1 >= 0:
                array[i][ii] += 1
            if ii+1 < size:
                array[i][ii] += 1

    if size == 0 or size2 == 0:
        print(array)
    else:
        for i in range(0,size2):
            for ii in range(0,size):
                print(array[i][ii], end=" ")
            print("")
    
    
    again = input("Would you like to go again? y/n ")
