import time

start_time = time.time()
valueFound = False
whichMod = 0
finalNumber = 0
n = 20
divisArray = [11,12,13,14,15,16,17,18,19,20]
while valueFound == False:
    whichMod = 0
    for i in range(0, len(divisArray)):
        if n % divisArray[i] == 0:
            whichMod +=1
    if whichMod == 10:
        finalNumber = n 
        valueFound = True
    n += 20
print(finalNumber)
print("--- %s seconds ---" % (time.time() - start_time))