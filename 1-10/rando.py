def HeronMethod(sourceNum, approx):
    count = 0
    sameNum = 0
    sameCount = 0
    sum = approx
    while sameNum != 3:
        resOne = sourceNum / sum
        resTwo = resOne + sum
        resThree = resTwo * 0.5
        sum = resThree
        print(sum)
        count += 1
        if count % 3 == 0:
            sameNum = sum
        if sameNum == sum:
            sameCount += 1
        if sameCount > 3:
            return sum


numOne = int(input("What number do you wanna find the square root of?"))
numTwo = int(input("What number do you want to approximate around: "))
result = HeronMethod(numOne, numTwo)
print("The square root of " + str(numOne) + " is " + str(result))