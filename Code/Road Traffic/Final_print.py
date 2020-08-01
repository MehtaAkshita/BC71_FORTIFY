o=open("Density_Count.txt","r")
for i in o:
    list(i)
mylist=i.split(',')
del mylist[-1]
for x in range(4):
    mylist[x]=int(mylist[x])
f=open("Output_signal_time.txt","r")
for j in f:
    list(j)
mylist2=j.split(',')
del mylist2[-1]
for k in range(0,len(mylist)):
    print("Density of cars from cam",k+1,"is",mylist[k],"and Updated Signal Time =",mylist2[k],"mins")
