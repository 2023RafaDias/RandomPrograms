array = input()
strike = []
for i in range(0,len(array)):
    if array[i] == "[" and array[i+1] not in "[]":
        strike[-1] += 1
    elif array[i] == "[" and array[i+1] == "]":
        strike.append(0)
        
print(strike)
    
