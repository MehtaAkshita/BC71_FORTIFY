import matplotlib.pyplot as plt
import csv

o=open("Density_Count.txt","r")
for i in o:
    list(i)
print(i)
print(o)
mylist=i.split(',')
del mylist[-1]
for x in range(4):
    mylist[x]=int(mylist[x])
   
#print(mylist)
sl=sum(mylist)
#print(sl)
lst=[]
def myround(x, base=5):
    return  round(x*base)/base
for a in range(4):
    j=mylist[a]*4/sl
    j=myround(j)
    lst.append(j)
    #print(lst[a])
f=open("Output_signal_time.txt","w+")
for c in lst:
    f.write(str(c)+",")
    #print(c)
f.close()
f1=open("Output_signal_time.txt","r+")


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



x = [1,2,3,4]
y = []

with open('Output_signal_time.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
    	y.append(row[0])
    	y.append((row[1]))
    	y.append((row[2]))
    	y.append((row[3]))
    	print(y)

plt.bar(x,y, label='Time')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Traffic Timing')
plt.legend()
plt.show()