again = "y"
while again == "y":
    n = int(input("Enter number here: "))
    n += 1
    count = 1
    count2 = 1
    while count2 != n:
        for i in range (1,count2+1):
            print(count, end=" ")
            count += 1
        print("")
        count2 += 1

    count2 -= 1
    while count2 != 0:
        count2 -= 1
        for i in range (1,count2+1):
            print(count, end=" ")
            count += 1
        print("")

    again = input("Again? y/n")
    
    
