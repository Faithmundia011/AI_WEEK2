# ----------------------------------------------
# AI for Sustainable Development - SDG 6: Clean Water
# K-Means Clustering for Water Pollution Analysis
# ----------------------------------------------

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Load Dataset
# (You can replace this with your actual dataset path or Kaggle water quality dataset)
url = "https://raw.githubusercontent.com/dphi-official/Datasets/master/water_quality.csv"
data = pd.read_csv(url)

# Step 2: Preview Data
print("Sample Data:")
print(data.head())

# Step 3: Select Relevant Features
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
            'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']
X = data[features]

# Step 4: Handle Missing Values
X = X.fillna(X.mean())

# Step 5: Normalize Data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Find Optimal Number of Clusters (Elbow Method)
inertia = []
K = range(2, 10)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(6,4))
plt.plot(K, inertia, 'bo-')
plt.title('Elbow Method to Determine Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()

# Step 7: Train K-Means Model (Assume optimal k = 3)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
data['Cluster'] = clusters

# Step 8: Evaluate Model
sil_score = silhouette_score(X_scaled, clusters)
print(f"Silhouette Score: {sil_score:.2f}")

# Step 9: Visualize Clusters
plt.figure(figsize=(8,5))
sns.scatterplot(x='ph', y='Turbidity', hue='Cluster', data=data, palette='viridis')
plt.title('Clusters of Water Quality Regions')
plt.xlabel('pH Level')
plt.ylabel('Turbidity')
plt.show()

# Step 10: Display Cluster Summary
print("\nCluster Characteristics:")
print(data.groupby('Cluster')[features].mean())
