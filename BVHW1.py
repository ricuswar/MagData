import matplotlib.pyplot as plt
import numpy as np

arr = [6,6,6,6,5,4,3,2,1,1,1,1,9,1,1,1,1,6,6,6,6,6,6]
arr1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mask = [1,-2,1]


for i in range(23):
    if i <= 0 :
        arr1[i] = arr[i]*mask[1] + arr[i]*mask[2]
    elif i >= 23 :
        arr1[i] = arr[i]*mask[1] + arr[i]*mask[0]
    else:
        for x in range(2):
            arr1[i] += arr[i]*mask[x]

#plt.figure()

#plt.subplot(411)
plt.plot(arr)
'''
plt.ylabel('Original')

plt.subplot(412)
plt.plot(np.gradient(arr))
plt.ylabel('First Dirv')

plt.subplot(413)
plt.plot(np.gradient(np.gradient(arr)))
plt.ylabel('Second Dirv')

plt.subplot(414)
'''
plt.plot(arr1)
plt.ylabel('Mask')

plt.show()