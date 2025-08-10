#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Importing the dataset
df = pd.read_csv('food.csv')
df = df[["Country","Value"]]
df = df.drop(columns=["Start Year", "End Year","Source"], errors="ignore")

#Defining the feature
X = df[["Value"]]

#Applying the Clustering
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df["Clusters"] = kmeans.fit_predict(X)

#Plotting the graph
plt.figure(figsize=(14,6))
plt.scatter(df['Country'], df['Value'], c=df['Clusters'], cmap='viridis', s=100)
plt.xticks(rotation=90)
plt.xticks(ticks=range(0, len(df), 5),
           labels=df['Country'].iloc[::5],
           rotation=90, ha='right')

plt.subplots_adjust(bottom=0.35)
plt.xlabel('Country')
plt.ylabel('Value')
plt.title('Clustering Countries by CO₂ Emissions')
plt.colorbar(label='Clusters')
plt.show()



