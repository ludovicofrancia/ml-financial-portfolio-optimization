© 2024 Ludovico Francia. All rights reserved.
# 📈 Machine Learning for Financial Portfolio Optimization

**ML-Powered Dynamic Asset Allocation using Random Forest and LSTM**

## 🔧 Tech Stack

`Python · Machine Learning · Random Forest · LSTM · Time Series · Portfolio Theory · NumPy · pandas · scikit-learn · SciPy`

## Project Overview

**Goal**

Design and evaluate machine learning models capable of **optimizing portfolio asset weights** to improve the risk-return trade-off, measured through the **Sharpe Ratio**.

**Approach**

Instead of predicting asset returns, I trained ML models to **directly predict optimal portfolio weights**, learned from historical data and macroeconomic indicators.

**Key Results**

- Random Forest–optimized portfolio achieved:
    - **+1.35% higher annual return**
    - **−0.22% lower annual volatility**
        
        compared to an equal-weighted benchmark
        
- LSTM showed lower prediction error but **worse return performance**
- Demonstrated that ML can enhance **asset allocation**, not just forecasting

## 🧠 Problem Context

### Why Portfolio Optimization Is Hard

Traditional portfolio construction (Modern Portfolio Theory) relies on:

- Historical averages
- Covariance matrices
- Static assumptions

These approaches struggle with:

- Non-linear relationships
- Regime changes
- High-dimensional data
- Macro-economic dynamics

### Research Question

> Can supervised machine learning models learn optimal asset allocation rules that outperform simple benchmark strategies?
> 

## 🧩 Key Innovation

### Predicting Weights, Not Returns

Most ML-based portfolio approaches:

- Predict future returns
- Then optimize weights downstream

⚠️ Problem: returns are **highly volatile and unbounded**

### My Approach

Following Zhang et al. (2020), I:

- Defined **portfolio weights** as the target variable
- Learned a direct mapping:
    
    **market state → optimal allocation**
    

**Why this works**

- Weights are bounded (0–1)
- Lower variance target
- Better learning stability
- Directly aligned with the investment decision

## 📊 Data & Inputs

### Assets

- Portfolio of **5 sector ETFs** (Euro Area)
- Additional market indicators:
    - Gold
    - Oil

### Time Horizon

- **10 years** of data
- June 2014 → May 2024
- Weekly frequency

### Macroeconomic Variables

- Interest rates (Euro Area)
- Inflation (HICP)

### Data Sources

- Yahoo Finance API
- Eurostat / FRED

## 🧹 Feature Engineering & Preprocessing

### Transformations

- Daily → weekly aggregation
- Log-returns for prices and volumes
- Log-changes for inflation
- Standardization of interest rates

### Temporal Features

- Monthly seasonality encoded via **one-hot variables**

### Why This Matters

These transformations:

- Improve distributional properties
- Stabilize variance
- Enhance ML convergence
- Preserve financial interpretability

## 🎯 Target Construction (Ground Truth)

### Objective

Maximize **Sharpe Ratio** subject to realistic constraints.

### Optimization Process

- Used `scipy.optimize.minimize`
- Optimized **negative Sharpe Ratio**

### Constraints

- Weights sum to 1
- Each weight ≤ 0.4 (avoid over-concentration)

The resulting **optimal weights** (computed ex-post) serve as:

- Training labels
- Benchmark “ground truth”

## 🤖 Models Implemented

### 1️⃣ Random Forest Regressor

- Captures non-linear interactions
- Robust to noise
- Strong performance with tabular data

**Why Random Forest**

- Interpretability
- Stability
- Lower overfitting risk than deep models

### 2️⃣ Long Short-Term Memory (LSTM)

- Designed for sequential data
- Learns temporal dependencies
- Suitable for financial time series

**Architecture**

- Sliding time windows
- Multivariate input sequences
- Regression output layer for portfolio weights

## 📐 Model Evaluation

### Prediction Accuracy

Metric: **Mean Squared Error (MSE)**

| Model | MSE | RMSE |
| --- | --- | --- |
| Random Forest | 0.032 | 17.9% |
| LSTM | 0.031 | 17.5% |

📌 *LSTM slightly better at predicting weights…*

## 📈 Portfolio Performance (What Really Matters)

### Benchmark

- Equal-weighted portfolio of same ETFs

### Random Forest Portfolio

- **+1.35% annual excess return**
- **−0.22% annual volatility**
- Higher Sharpe Ratio
- Better cumulative performance curve

📌 *Best overall performer*

### LSTM Portfolio

- Lower volatility
- Lower average return
- Underperformed both Random Forest and benchmark

📌 *Lower error ≠ better investment outcome*

## 🧠 Key Insights

- **Prediction accuracy alone is not enough**
- Financial performance must be evaluated at the **portfolio level**
- Tree-based models can outperform deep learning in structured financial data
- ML can enhance asset allocation **without forecasting prices**

## 💼 Practical Implications

This approach can be applied to:

- Systematic asset allocation
- Robo-advisory strategies
- Tactical portfolio rebalancing
- Risk-aware investment systems

## 🚀 What I’d Improve Next

- Extend dataset before 2014
- Increase number of assets
- Perform regime-specific analysis
- Add transaction costs
- Explore:
    - Gradient Boosting
    - Reinforcement Learning
    - NLP-based sentiment features