import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,25,25,15])
xlabels=["apple","banana","dates","cherries"]
plt.pie(x,labels=xlabels)

plt.show()