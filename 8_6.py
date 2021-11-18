import numpy as np
def bubbleSort(arr):
    n = len(arr)
    #遍历所以元素
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
a = np.random.randint(1,100,size=10)
bubbleSort(a)
print("排序结果：",a)