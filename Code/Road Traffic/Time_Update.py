mylist=[4,2,1,1]
sl=sum(mylist)
lst=[]
def myround(x, base=4):
    return  round(x*base)/base
for a in range(4):
    j=mylist[a]*4/sl
    j=myround(j)
    lst.append(j)
    #print(lst[a])

print(lst)
