l=list(map(str,input().split()))
l.sort()
l.sort(key=len)
print(l)