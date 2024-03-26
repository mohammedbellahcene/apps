import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
taille=np.random.normal(1.76,0.10,10)
poids=np.random.normal(70,10,10)
imc=poids/taille**2
plt.scatter(poids,imc)
plt.show()