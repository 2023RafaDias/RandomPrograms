digit = [0,0,0]
number = int(input())

for i in range(1,4):
    digit[-i] = number%2
    number = number//2

print(digit) 
