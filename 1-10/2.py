n = 1
numOne = 1
numTwo = 0
sum = 0
numMod = []
while n < 4000000:
    n = numOne + numTwo
    numTwo, numOne = numOne, n
    if n %2 == 0:
        numMod.append(n)

for i in range(0,len(numMod)):
    sum += numMod[i]

print(sum)