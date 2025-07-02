l=[1,43,4,64,3,73,2,7]
#t=tuple(l)
#print("largest element of list:",max(t))
l.sort()
print("largest element of list:",l[-1])
print("2nd largest element of list:",l[-2])
sum=0
for i in l:
    sum=sum+i
avg=sum/len(l)
print("Average of list:",avg)

