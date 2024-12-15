n,c1,c2 = input().split()
n = int(n)
slist = list(input())

for i in range(n):
    if slist[i] != c1:
        slist[i] = c2
    
s = ''.join(slist)
print(s)
