#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField ,MarkovTransitionField

path="D:\\研究所\\雷射切割\\0529\\power data\\"
list_data=os.listdir(path)

list_data.sort(key=lambda x: tuple(map(int, x[:-4].split("-"))))
print(list_data)
#%%
for x in list_data:
    path_data= path+x
    name=x.split(".")
    print(x,name[0])
#%%
a= np.random.randn(20,20)
gasf=GramianAngularField(image_size =20,method='summation')
a_gasf=gasf.fit_transform(a)
plt.imshow(a)
plt.show()