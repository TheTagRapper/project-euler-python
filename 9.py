valueFound = False
n = 1
while valueFound == False:
    c = 0
    j = 1
    #Using Ozanam's Method to find a non-composite Pythag Triple
    denom = 4 * n + 4
    numer = (n * denom) + (4*n) + 3
    hyp = numer + 2
    #Finding the composite variants of that Pythag Triple until the sum is greater than 1000
    compDenom = denom
    compNumer = numer
    compHyp = hyp
    while c < 1000:
        compDenom = denom * j
        compNumer = numer * j
        compHyp = hyp * j
        j += 1
        c = compDenom + compNumer + compHyp
        with open("output.txt", "a") as file:
            stringEnd = str(compDenom) + " " + str(compNumer) + " " +  str(compHyp) + " " + str(c)
            file.write(stringEnd + "\n")
            file.close()

    if c == 1000:
        valueFound = True
        break
    n += 1
print(str(compDenom * compNumer * compHyp))