import missingno as mg
import pandas as pd
import matplotlib.pyplot as plt 
gold = pd.read_csv('LBMA-GOLD.csv')
mg.matrix(gold)
plt.show()