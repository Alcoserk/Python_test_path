n=input()
txt='1'
k=1
while str(k)!=n:
    k=k-1
    txt=txt+"+"+str(k)
print(txt, '=', eval(txt))
