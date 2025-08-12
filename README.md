# Dimensionality Reduction for a Sloan Digital Sky Survey Galaxy Sample

This repository contains my final project for a university Machine Learning course.  
The project explores and compares dimensionality reduction techniques to analyze emission-line galaxy data from the Sloan Digital Sky Survey (SDSS).


## Introduction

Dimensionality reduction helps simplify high-dimensional datasets by reducing the number of features while preserving important structures and patterns.  
In astronomy, galaxy spectra can have many correlated features, making them good candidates for dimensionality reduction before classification or visualization.

The goals of this project were to:
- Apply PCA, t-SNE, and UMAP to galaxy emission line data
- Visualize the data
- Compare methods in terms of clarity of separation between galaxy types


## Repository Structure
```bash
dimensionality-reduction-sdss/
├── data/ # SDSS dataset
├── src/ # Python scripts
├── results/ # generated plots
├── requirements.txt
├── README.md
└── LICENSE
```


## Dataset

The dataset contains emission line flux measurements for galaxies observed by the SDSS.  
Each row corresponds to one galaxy, with the following key flux features: h_beta_flux, h_alpha_flux, oiii_5007_flux, nii_6584_flux, sii_6717_flux, sii_6731_flux, oi_6300_flux, which correspond to intensities of emission lines (with wavelengths given in nanometers included in the feature names) produced by H, Si, Ni and O atoms. Those intensities are correlated with the chemical composition of a given galaxy, and help us to differentiate between galaxies depending on the way they were created.

From these fluxes, we also compute standard **BPT diagram ratios**:
- O3Hb = log([OIII]5007 / Hβ)
- N2Ha = log([NII]6584 / Hα)
- S2Ha = log(([SII]6717 + [SII]6731) / Hα)
- O1Ha = log([OI]6300 / Hα)

## Methods & Results

### **BPT Diagrams**
Baldwin–Phillips–Terlevich (BPT) diagrams are used in astrophysics to distinguish between:
- Emission-Line (EL) galaxies — ionized gas from star formation
- Active Galactic Nuclei (AGN) — ionization from non-thermal sources like black holes

| [NII]/Hα vs [OIII]/Hβ | [SII]/Hα vs [OIII]/Hβ | [OI]/Hα vs [OIII]/Hβ |
|---|---|---|
| ![](results/bpt_nii.png) | ![](results/bpt_sii.png) | ![](results/bpt_oi.png) |

### **PCA**
Explained variance and galaxy projections in reduced dimensions.

Non-linear projection emphasizing local structures.

![](results/pca_variance.png)

| PCA 2D Projection | PCA 3D Projection | PCA 2D Projection zoom-in |
|---|---|---|
| ![](results/pca_2d.png) | ![](results/pca_3d.png) | ![](results/pca_2d_zoom.png) |

---

### **t-SNE**
Non-linear projection emphasizing local structures.

| PCA 2D Projection | PCA 3D Projection |
|---|---|
| ![](results/tsne_ppx30.png) | ![](results/tsne_ppx50.png) |


---

### **UMAP**
Preserves local & global structures efficiently.

| UMAP 2D | UMAP 3D |
|---|---|
| ![](results/umap_2d.png) | ![](results/umap_3d.png) |

---

