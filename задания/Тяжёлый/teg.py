pah1 = open('pah.txt')
van1 = open('van.txt')
pah = [int(x) for x in pah1]
van = [int(x) for x in van1]
p = pah[7]
v = van[7]
sumpa = sum(pah) - p
sumva = sum(van) - v 
if sumpa > sumva:
    print(sumpa, p)
else:
    print(sumva, v)
