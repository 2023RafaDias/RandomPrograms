x = int(input())
size = x*2-1
row = []
for i in range(size):
    row.append([])
    if i <= x-1:
        row[-1] =(i-x+2)
    else:
        row[-1]=(x-i)

for ii in range(0,size):
    for i in range(0,size):
        if i <= size-2:
            if row[i] <= 0:
                print(" ", end = " ")
            else:
                print(row[i], end = " ")

            if ii < x-1:
                row[i]+=1
            else:
                row[i]-=1
        else:
            if row[i] <= 0:
                print(" ")
            else:
                print(row[i])

            if ii < x-1:
                row[i]+=1
            else:
                row[i]-=1


