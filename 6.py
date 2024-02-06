sum_nattysquared = 0
sumsquared_natty = 0
for i in range(0,101):
    temp = i ** 2
    sum_nattysquared += temp
for j in range(0,101):
    sumsquared_natty += j
sumsquared_natty = sumsquared_natty ** 2
output =sumsquared_natty - sum_nattysquared 
print(output)