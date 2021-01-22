import primefac, sys

def aliquotSum(n):
    sm = 0
    for i in range(1,n):
        if (n % i == 0):
            sm = sm + i
    return sm # return sum

def perfectIndex(n): # see how close the aliquot sum is to one
	m = aliquotSum(n)
	if m > n:	return float(n) / float(m)
	if m < n:	return float(m) / float(n)

print(perfectIndex(int(sys.argv[1])))
print(aliquotSum(int(sys.argv[1])))

#x = oddNearPerfect(int(sys.argv[1]), 0.995)
#print(str(x[0]) + " " + str(x[1]))
