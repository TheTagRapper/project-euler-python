import time
import numpy as np

start_time = time.time()
arrayLength = 2000000
baseArray = np.ones(arrayLength , dtype=bool)
n = 2
while n * n < arrayLength:
    if baseArray[n-2] == True:
        i = n
        while n * i < arrayLength:
            baseArray[(n * i) - 2] = False
            i+= 1
    n += 1

total = 0
with open("output.txt", "w") as file:
    for i in range(1 , arrayLength-1):
        if baseArray[i-1] == True:
            file.write(str(i+1) +"\n")
            total += (i+1)
    file.write(str(total))
    file.close()
print("Process took " + str(time.time() - start_time) + " seconds.")