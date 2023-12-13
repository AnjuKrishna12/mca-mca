



# Load your wine dataset (replace 'WineQuality - WineQuality.csv' with the actual file path)
df = pd.read_csv('WineQuality - WineQuality.csv')
print(df.head())

# Select the relevant features for clustering
features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']

# Extract the selected features for clustering
X = df[features]

# Impute missing values with mean
X = X.fillna(X.mean())

# Standardize the features (important for KMeans)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose the number of clusters
n_clusters = 2  # Change to 2 for red and white wine

# Create a KMeans model with explicit n_init
kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)

# Fit the model to the standardized data
kmeans.fit(X_scaled)

# Map cluster labels to wine types
cluster_type_mapping = {
    0: 'Red',
    1: 'White'
}

# Convert cluster labels to Pandas Series and map to wine types
df['Cluster'] = pd.Series(kmeans.labels_).map(cluster_type_mapping)

print("Cluster Counts:")
print(df['Cluster'].value_counts())

# Visualize the clusters using PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Assuming df['Cluster'] contains string labels like 'yellow' and 'Blue'
colors = {'yellow': 'yellow', 'Blue': 'violet'}


# Scatter plot for the original data with cluster colors
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['Cluster'].map({'Red': 0, 'White': 1}), cmap='viridis', marker='o', alpha=0.8)
plt.title('KMeans Clustering of Wine Quality Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# Create new data points for prediction (replace with your actual data)
new_data = pd.DataFrame({
    'fixed acidity': [7.0, 6.5, 8.2],
    'volatile acidity': [0.3, 0.4, 0.2],
    'citric acid': [0.4, 0.2, 0.3],
    'residual sugar': [2.5, 1.8, 2.0],
    'chlorides': [0.05, 0.06, 0.04],
    'free sulfur dioxide': [20, 25, 18],
    'total sulfur dioxide': [80, 90, 75],
    'density': [0.996, 0.995, 0.997],
    'pH': [3.2, 3.4, 3.1],
    'sulphates': [0.5, 0.4, 0.6],
    'alcohol': [12.0, 11.5, 12.5],
    'quality': [0, 0, 0]  # Placeholder for quality, adjust based on your data
})

# Standardize the new data using the same scaler used for training
new_data_scaled = scaler.transform(new_data)

# Predict the cluster labels for the new data
new_data_clusters = kmeans.predict(new_data_scaled)

# Map cluster labels to wine types
new_data['Cluster'] = pd.Series(new_data_clusters).map(cluster_type_mapping)

# Display the new data with assigned clusters
print("New Data with Predicted Clusters:")
print(new_data)