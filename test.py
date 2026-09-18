import numpy as np

a = np.array([1, 2, 3, 4])           # 从列表创建
b = np.zeros((2, 3))                 # 2行3列，全是0
c = np.arange(0, 10, 2)              # 0到10，步长2 → [0,2,4,6,8]
d = np.linspace(0, 1, 5)             # 0到1之间，均匀取5个数
e = np.random.rand(2, 3)             # 2行3列，随机数
np.random.seed(111231234)
print(np.random.rand(2,3))          # 3行2列，随机数