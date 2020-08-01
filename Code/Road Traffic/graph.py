import matplotlib.pyplot as plt
import csv

x = [1,2,3,4]
y = []

with open('Density_Count.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
    	y.append(int(row[0]))
    	y.append(int(row[1]))
    	y.append(int(row[2]))
    	y.append(int(row[3]))
    	print(y)

plt.bar(x,y, label='Cars')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Count of cars')
plt.legend()
plt.show()


