"""N C M

1) numero de figutinhas  10
2) numero de figurinhas raras  2
3) numero de figurinhas ja compradas  5

todas as figurinhas q sao carimbadas 4 7

figurinhas q sao compradas 7 1 2 8 3"""

first = [0,0,0]
hold = input()
print(hold.replace(" ", ""))
for i in range(0,3):
    first[i] = int(hold[i])

second = []
hold = input()
print(hold.replace(" ", ""))
for i in range(0,len(hold)):
    second.append(int(hold[i]))


third = []
hold = input()
print(hold.replace(" ", ""))
for i in range(0,len(hold)):
    third.append(int(hold[i]))

print(first)
print(second)
print(third)
