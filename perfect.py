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

def oddNearPerfect(start_n, threshold): # find odd numbers that are close to being perfect numbers
	index = 0
	n = start_n
	while index < threshold:
		n += 2
		if (n % 5000) < 2:	print(n)
		index = perfectIndex(n)
#	print(index)
	return [n, aliquotSum(n)]

x = oddNearPerfect(int(sys.argv[1]), 0.995)
print(str(x[0]) + " " + str(x[1]))
