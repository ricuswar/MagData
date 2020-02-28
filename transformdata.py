import matplotlib.pyplot as plt
import numpy as np
import csv
import seaborn as sb

x=[]
y=[]

with open('xandy.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

x=np.array(x)
y=np.array(y)

data = np.vstack((y,x)).T

heatmap = sb.heatmap(data)

plt.show()

'''
plt.plot(x,y, marker='o')

plt.title('MagData')

plt.xlabel('Time')
plt.ylabel('z-axis on magnetometer')

plt.show()
'''