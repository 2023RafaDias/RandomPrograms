import ast
x = ast.literal_eval(input())

for i in range(0,len(x[0])):
    for j in range(0,len(x[0][0])):
        x[0][i][j]+=x[1][i][j]
print(x[0])

