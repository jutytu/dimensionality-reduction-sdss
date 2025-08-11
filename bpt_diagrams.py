import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Sample of line emission fluxes in galaxies.csv')
print(df.head())
print('Columns: ', df.columns.tolist())


# DATA WE WANT

features = [
    'h_beta_flux', 'h_alpha_flux', 'oiii_5007_flux',
    'nii_6584_flux', 'sii_6717_flux', 'sii_6731_flux', 'oi_6300_flux'
]


# LOG RATIOS

df['O3Hb'] = np.log10(df['oiii_5007_flux'] / df['h_beta_flux'])
df['N2Ha'] = np.log10(df['nii_6584_flux'] / df['h_alpha_flux'])
df['S2Ha'] = np.log10((df['sii_6717_flux'] + df['sii_6731_flux']) / df['h_alpha_flux'])
df['O1Ha'] = np.log10(df['oi_6300_flux'] / df['h_alpha_flux'])


# PLOTS

# [NII]/Hα vs [OIII]/Hβ
plt.figure(figsize=(8, 6))
plt.scatter(df['N2Ha'], df['O3Hb'], s=5, alpha=0.2)
plt.xlabel('log([NII]6584 / Hα)')
plt.ylabel('log([OIII]5007 / Hβ)')
plt.title('BPT Diagram: [NII]/Hα vs [OIII]/Hβ')
plt.grid(True)
plt.tight_layout()
x = np.linspace(-2, 0.3, 100)
y = (0.61 / (x - 0.47)) + 1.19
plt.plot(x, y, 'k--') # EL vs ANG
plt.show()

# [SII]/Hα vs [OIII]/Hβ
plt.figure(figsize=(8, 6))
plt.scatter(df['S2Ha'], df['O3Hb'], s=5, alpha=0.2)
plt.xlabel('log([SII]6717+6731 / Hα)')
plt.ylabel('log([OIII]5007 / Hβ)')
plt.title('BPT Diagram: [SII]/Hα vs [OIII]/Hβ')
plt.grid(True)
plt.tight_layout()
plt.show()

# [OI]/Hα vs [OIII]/Hβ
plt.figure(figsize=(8, 6))
plt.scatter(df['O1Ha'], df['O3Hb'], s=5, alpha=0.2)
plt.xlabel('log([OI]6300 / Hα)')
plt.ylabel('log([OIII]5007 / Hβ)')
plt.title('BPT Diagram: [OI]/Hα vs [OIII]/Hβ')
plt.grid(True)
plt.tight_layout()
plt.show()