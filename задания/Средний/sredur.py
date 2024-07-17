f = open('sredur.txt')
a = [int(x) for x in f]
col = 0
chis = 0
for i in range(1,21):
    cl = a.count(i)
    if cl > col:
        col = cl
        chis = i
print(chis, col)
    
    

    
