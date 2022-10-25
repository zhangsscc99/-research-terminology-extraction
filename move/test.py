lst=[1,2,3,4,5]
with open("result.txt",'w') as f:
    for item in lst:

        f.write("%d\n"%item)
f.close()