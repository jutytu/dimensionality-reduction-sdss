import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import umap


df = pd.read_csv('Sample of line emission fluxes in galaxies.csv')

features = [
    'h_beta_flux', 'h_alpha_flux', 'oiii_5007_flux',
    'nii_6584_flux', 'sii_6717_flux', 'sii_6731_flux', 'oi_6300_flux']

X = df[features].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X.shape) 
    

embedding_2d = umap.UMAP(n_neighbors=15, min_dist=0.001, n_components=2).fit_transform(X_scaled)

# 3D
embedding_3d = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=3).fit_transform(X_scaled)

# plot 2D

plt.figure(figsize=(8, 6))
plt.scatter(embedding_2d[:, 0], embedding_2d[:, 1], s=2, alpha=0.7)
plt.title("Projection 2D - galaxies with UMAP")
plt.xlabel("UMAP 1")
plt.ylabel("UMAP 2")
plt.grid(True)
plt.show()


# plot 3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(embedding_3d[:, 0], embedding_3d[:, 1], embedding_3d[:, 2], s=0.5, alpha=0.5, c='green')
ax.set_title("Projection 3D - galaxies with UMAP")
ax.set_xlabel("UMAP 1")
ax.set_ylabel("UMAP 2")
ax.set_zlabel("UMAP 3")
plt.show()