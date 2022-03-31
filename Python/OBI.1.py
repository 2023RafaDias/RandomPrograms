import random
chairs = [0,1,2]
A, B = random.randint(1,1000),random.randint(1,1000)

if A % 3 == 1:
    A = 0
elif A % 3 == 2:
    A = 1
else:
    A = 2

if B % 3 == 1:
    B = 0
elif B % 3 == 2:
    B = 1
else:
    B = 2

if A == B:
    if B == 2:
        B = 0
    else:
        B += 1

for i in range (0,3):
    if chairs[i] != A and chairs[i] != B:
        C = chairs[i]
print("Carolina = ",C)
