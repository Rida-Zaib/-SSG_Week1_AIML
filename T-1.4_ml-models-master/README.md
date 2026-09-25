# Task 1.4 — Two ML Models with Scikit-learn

## Overview
Builds and evaluates two machine learning models with scikit-learn: one regression
model and one classification model, each with preprocessing, a train/test split,
and proper evaluation metrics.

## Datasets
Both datasets are built into scikit-learn, so no external download is needed:
- **Diabetes dataset** — used for regression, predicts disease progression from
  10 baseline health measurements.
- **Breast cancer dataset** — used for classification, predicts whether a tumor
  is malignant or benign from 30 measured features.

## Part 1: Regression
- Model: Linear Regression
- Preprocessing: features scaled with `StandardScaler`
- Split: 80/20 train/test
- Metrics: MSE (mean squared error) and R² score

## Part 2: Classification
- Model: Logistic Regression
- Preprocessing: features scaled with `StandardScaler`
- Split: 80/20 train/test
- Metrics: accuracy, precision, recall, F1 score, and confusion matrix

## Files
- `ml_models.ipynb` — the full notebook, both models, code + outputs + evaluation report

## How to run
```bash
pip install scikit-learn pandas
jupyter notebook ml_models.ipynb
```
Then Run All Cells.

## Evaluation report
- **Regression:** R² score shows how much of the variance in disease progression
  the model explains; lower MSE means predictions are closer to actual values.
- **Classification:** accuracy, precision, recall and F1 all come out high since
  the breast cancer dataset is fairly easy to separate; the confusion matrix shows
  exactly how many malignant vs. benign cases were classified correctly.

## Deliverable
Notebook with two trained models + evaluation report, as required by the Skill Set
Go EduTech AI/ML track, Week 1, Task 1.4.
