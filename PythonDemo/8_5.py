import numpy as np
#导入numpy库
Z = np.random.random((5,5))
Zmax,Zmin = Z.max(),Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)