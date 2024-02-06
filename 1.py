n=0
numbersMod = []
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        numbersMod.append(n)
    n += 1
sum = 0
for i in range(0, len(numbersMod)):
    sum += numbersMod[i]

print(sum)