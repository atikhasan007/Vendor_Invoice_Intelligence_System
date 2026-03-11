# Vendor Invoice Intelligence System
**Freight Cost Prediction & Invoice Risk Flagging**

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Business Objectives](#business-objectives)  
- [Data Sources](#data-sources)  
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
- [Models Used](#models-used)  
- [Evaluation Metrics](#evaluation-metrics)  
- [End-to-End Application](#end-to-end-application)  
- [Project Structure](#project-structure)  
- [How to Run This Project](#how-to-run-this-project)  
- [Author & Contact](#author--contact)  

---

## Project Overview
This project implements an **end-to-end machine learning system** to support finance teams by:  

1. **Predicting expected freight cost** for vendor invoices.  
2. **Flagging high-risk invoices** that require manual review due to abnormal cost, freight, or operational patterns.  

---

## Business Objectives

### 1. Freight Cost Prediction (Regression)
**Objective:**  
Predict the expected freight cost for a vendor invoice using quantity, invoice value, and historical behavior.  

**Why it matters:**  
- Freight is a significant component of landed cost.  
- Poor freight estimation impacts margin analysis and budgeting.  
- Early prediction improves procurement planning and vendor negotiation.  

### 2. Invoice Flagging (Classification)
**Objective:**  
Identify invoices with abnormal patterns in cost, freight, or delivery that may require **manual review**.  

**Why it matters:**  
- Manual review is time-consuming.  
- Early detection of anomalies reduces financial risk.  
- Prioritizes human intervention where it adds the most value.  

---
<img width="932" height="833" alt="image" src="https://github.com/user-attachments/assets/d9b6464c-f8ac-46c4-a672-bca8f252c975" />

## Data Sources
Data is stored in a **SQLite database (`inventory.db`)** with the following tables:  

- **vendor_invoice** — Invoice-level financial and timing data  
- **purchases** — Item-level purchase details  
- **purchase_prices** — Reference purchase prices  
- **begin_inventory**, **end_inventory** — Inventory snapshots  

> SQL aggregation is used to generate invoice-level features.

---

## Exploratory Data Analysis (EDA)
EDA focuses on **business-driven questions**:  

- Do flagged invoices have higher financial exposure?  
- Does freight scale linearly with quantity?  
- Does freight cost depend on invoice value or purchase quantity?  

**Techniques used:**  
- Summary statistics  
- Visualizations (histograms, scatter plots)  
- Statistical tests (t-tests) to confirm differences between flagged and normal invoices  

---

## Models Used

### Regression (Freight Prediction)
- **Linear Regression** (baseline)  
- **Decision Tree Regressor**  
- **Random Forest Regressor** (final model)  

### Classification (Invoice Flagging)
- **Logistic Regression** (baseline)  
- **Decision Tree Classifier**  
- **Random Forest Classifier** (final model with GridSearchCV)  

> Hyperparameter tuning is performed using **GridSearchCV** with **F1-score** to handle class imbalance.

---

## Evaluation Metrics

### Freight Prediction
- **MAE** — Mean Absolute Error  
- **RMSE** — Root Mean Squared Error  
- **R² Score**  

### Invoice Flagging
- **Accuracy**  
- **Precision**  
- **Recall**  
- **F1-score**  
- **Classification Report**  
- **Feature Importance Analysis**  

---

## End-to-End Application
A **Streamlit application** demonstrates the complete workflow:  

- Input invoice details  
- Predict expected freight cost  
- Flag high-risk invoices in real time  
- Provide human-readable explanations  

---

## How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/inventory-invoice-analytics.git
cd inventory-invoice-analytics
