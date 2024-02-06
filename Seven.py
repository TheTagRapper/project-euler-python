import time
start_time = time.time()
primeNum = 0
p=2
x = 3
carmichael_numbers_k2 = [
    561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341,
    41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401,
    172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041
]
carmichael_numbers_k3 = [
    561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341,
    41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401,
    172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041
]
#Using AKS Test
while primeNum != 10011:
    a = 2 ** p
    b = 2 ** p - 1
    c = a - b
    if c % p == 0:
        primeNum += 1
    p += 1
print(p-1)
durationTime = time.time() - start_time
print("Time taken: " + str(durationTime) + " seconds")

#True value is 104743
