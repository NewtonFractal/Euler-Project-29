import time
terms = []
start = time.time()

def Distinct_powers(n):
    for x in range(2,n):
        for y in range(2,n):
            terms.append(x**y)

Distinct_powers(101)

print(len(set(terms)))


end = time.time()
print(end - start)