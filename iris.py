#Write a Python program to load the Iris data from a csv file into a dataframe,
#print the shape of the data, type of the data and first 3 rows.
#Create a plot to get a General Statistics of the Iris dataset.

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\HH\\Desktop\\Iris\\Iris.csv")
print("Shape of the data:")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 3 rows:")
print(data.head(3))

data.describe().plot(kind = "area",fontsize=16, figsize = (15,8), table = True, colormap="Accent")
plt.xlabel('Statistics',)
plt.ylabel('Value')
plt.title("General Statistics of Iris Dataset")
plt.show()

