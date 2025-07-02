a=input("Enter a string:")
dict={}
c=("a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
for i in range(len(a)):
    if(a[i] in dict.keys()):
        dict[a[i]]=dict[a[i]]+1
    else:
        dict[a[i]]=1

print("Alphabate","No of occurence",sep="\t")

b=dict.keys()
for i in c:
    if (i in b):
        print(i,dict[i],sep="\t")
    else:
        print(i,0,sep="\t")