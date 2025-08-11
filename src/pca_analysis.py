import pandas as pd

df = pd.read_csv('Sample of line emission fluxes in galaxies.csv')

features = [
    'h_beta_flux', 'h_alpha_flux',
    'oiii_5007_flux', 'nii_6584_flux',
    'sii_6717_flux', 'sii_6731_flux', 'oi_6300_flux'
]

X = df[features].values

from sklearn.preprocessing import StandardScaler # scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X.shape)  


from sklearn.decomposition import PCA

pca = PCA(n_components=7)
X_pca = pca.fit_transform(X_scaled)


import matplotlib.pyplot as plt

explained = pca.explained_variance_ratio_
cumulative = explained.cumsum()

plt.figure(figsize=(6, 4))
plt.plot(range(1, 8), explained, marker='o', label='Individual')
plt.plot(range(1, 8), cumulative, marker='s', label='Cumulative')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance (All Fluxes)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

for i, component in enumerate(pca.components_):
    print(f"PC{i+1} = ", end="")
    terms = [f"{coef:.3f}×{name}" for coef, name in zip(component, features)]
    print(" + ".join(terms))



plt.figure(figsize=(6, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], s=20, alpha=0.6, color='teal')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('2D PCA Projection (All Fluxes)')
plt.grid(True)
plt.tight_layout()
plt.xlim([-0.04195, -0.0417])  # zoom-in of the cluster
plt.ylim([0.00145, 0.0018])
plt.show()
print(f"Number of samples in PCA projection: {X_pca.shape[0]}")
print(X_pca[:, 0])
print(X_pca[:, 1])


fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], s=20, alpha=0.6, color='darkorange')

ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
ax.set_title('3D PCA Projection (All Fluxes)')
plt.tight_layout()
plt.show()