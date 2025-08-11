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

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, perplexity=50, random_state=42, learning_rate='auto', verbose=10)
X_tsne = tsne.fit_transform(X_scaled)

import matplotlib.pyplot as plt

plt.figure(figsize=(7, 5))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], s=10, alpha=0.6, color='crimson')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.title('t-SNE Projection (2D)')
plt.grid(True)
plt.tight_layout()
plt.show()