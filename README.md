# **Synthetic Manufacturing Data Generation with Generative AI**

My aim is to explore and address the issue of data scarcity in industrial manufacturing processes by leveraging both traditional machine learning techniques and generative AI approaches. Specifically, I focus on two core challenges:

1. **Steel Plate Defect Classification** – Developing robust models to accurately classify surface defects in stainless steel plates using geometric and luminosity indicators, despite limited labeled data.  
2. **Bending Machine Process Optimization** – Enhancing the performance of tube bending machines by optimizing key process parameters to achieve improved manufacturing outcomes.

By employing generative AI methods to create synthetic data, I aim to overcome the limitations posed by small or imbalanced datasets, improve model generalization, and ultimately contribute to the development of more reliable and intelligent manufacturing systems.

## Datasets

### 1. Steel Plate Defect Dataset
**Source**: Semeion Research Center of Sciences of Communication  
**Features**: 27 indicators describing geometric properties of steel plate defects  
**Target Classes**: 7 defect types (one-hot encoded)
- Pastry
- Z_Scratch
- K_Scatch
- Stains
- Dirtiness
- Bumps
- Other_Faults

**Key Features**:
- X/Y Minimum/Maximum coordinates
- Pixels_Areas
- X/Y_Perimeter
- Luminosity metrics
- Various geometric indices
- Steel type and thickness

### 2. Tube Bending Machine Dataset
**Features**:
- Test No
- Tube outer diameter (mm)
- Tube wall thickness (mm)
- Bending angle (°)
- The distance of the mandrel (mm)
- Mandrel type
- Test Result (target variable)

## Methodology

### Traditional Machine Learning Approaches
- **XGBoost** (Gradient Boosted Trees)
- Random Forest
- Support Vector Machines (SVM)
- Logistic Regression (for classification)
- Neural Networks

### Generative AI Techniques for Synthetic Data
1. **Tabular GANs** (Generative Adversarial Networks)
   - CTGAN
   - TVAE (Tabular VAE)
   
2. **Variational Autoencoders (VAEs)**
   - Standard VAEs for tabular data
   - Conditional VAEs for targeted generation

3. **Gaussian Mixture Models (GMM)**
   - For modeling multivariate distributions
   - Combined with oversampling techniques

### Evaluation Framework
- Performance comparison between:
  - Models trained on original data only
  - Models trained on synthetic data only
  - Models trained on augmented (original + synthetic) data
- Metrics: Accuracy, Precision, Recall, F1-score (classification); RMSE, MAE (regression)

## Project Structure

```
#TODO                          
```

## Requirements
- Python 3.7+
- Key libraries:
  - pandas, numpy
  - scikit-learn, xgboost
  - sdv (Synthetic Data Vault) for tabular GANs/VAEs
  - matplotlib, seaborn for visualization

