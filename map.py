
import gmplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
df= pd.read_csv("/Users/tingjue/170 project/map.csv",index_col=0)

gmap = gmplot.GoogleMapPlotter(35, -102, 5)


gmap.heatmap(df['lat'], df['long'],threshold = 1, radius=18, opacity=1)

gmap.draw('gmplot.html')

"""
cars= pd.read_csv("/Users/tingjue/170 project/cars4.csv",index_col=0)
cor = cars[['price','year','avg_rating','count','odometer']]
corrMatrix = cor.corr()
#sns.heatmap(corrMatrix, annot=True)
#plt.show()
plt.figure(figsize=(10, 10))
sns.set(font_scale=1.6)
ax = plt.axes()
g =sns.heatmap(corrMatrix, annot=True, ax = ax,cmap = "RdBu_r",annot_kws={"fontsize":20})

ax.set_title('Correlation Heatmap',fontsize = 15)
plt.show()
