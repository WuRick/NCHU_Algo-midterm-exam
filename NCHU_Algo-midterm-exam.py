#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time
import math
import matplotlib.pyplot as plt

def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return i
    return -1

def binary_search(S, x):
    left, right = 0, len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == x:
            return mid
        elif S[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def fibonacci_search(S, x):
    # 初始化 Fibonacci 数列
    fib2, fib1 = 0, 1
    while fib1 <= len(S):
        fib2, fib1 = fib1, fib1 + fib2

    # 执行搜索
    offset = -1
    while fib1 > 1:
        i = min(offset + fib2, len(S) - 1)
        if S[i] < x:
            fib1, fib2, offset = fib2, fib1 - fib2, i
        elif S[i] > x:
            fib1, fib2 = fib2 - fib1, fib1 - fib2
        else:
            return i
    if fib1 and S[offset+1] == x:
        return offset+1
    return -1

def linear_search_time(n):
    lst = list(range(n))
    start_time = time.time()
    linear_search(lst, n-1)
    end_time = time.time()
    return (end_time - start_time) * 1000

def binary_search_time(n):
    lst = list(range(n))
    start_time = time.time()
    binary_search(lst, n-1)
    end_time = time.time()
    return (end_time - start_time) * 1000

def fibonacci_search_time(n):
    lst = list(range(n))
    start_time = time.time()
    fibonacci_search(lst, n-1)
    end_time = time.time()
    return (end_time - start_time) * 1000

# 產生 x 軸數據
x = [10 ** i for i in range(1, 6)]

# 產生 y 軸數據
y1 = [linear_search_time(n) for n in x]
y2 = [binary_search_time(n) for n in x]
y3 = [fibonacci_search_time(n) for n in x]

# 畫出三條線圖
fig, ax = plt.subplots()
ax.plot(x, y1, label="Linear Search")
ax.plot(x, y2, label="Binary Search")
ax.plot(x, y3, label="Fibonacci Search")
ax.set_xlabel("Size of input (n)")
ax.set_ylabel("Execution time (ms)")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend()
plt.show()


# In[ ]:




