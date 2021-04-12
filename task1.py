n='abbabbaabab'
for i in range(1,len(n)):
    for j in range(0,i):
        a=n[i:j]
        if a==a[::-1]:
            print(a)
