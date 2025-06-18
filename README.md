# 🏠 House Price Prediction - Machine Learning Web Application

This project demonstrates a **machine learning-based system to predict house prices** based on multiple property features. It includes data exploration, visualization, model training, and an interactive web application for real-time price predictions.

---

## 📋 Project Overview

- **Goal:** Predict the market price of a house using property attributes.
- **Tech Stack:** Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Streamlit.
- **Model:** Linear Regression trained on a real estate dataset.
- **Features:** 13 input features including area, bedrooms, furnishing status, and others.
- **Visualization:** Data analysis and feature relationships explored using Matplotlib and Seaborn.
- **UI:** User-friendly web interface built with Streamlit for live predictions.

---

## 🧮 Data Features

| Feature                      | Description                             |
|-----------------------------|-----------------------------------------|
| `area`                      | Size of the house in square feet       |
| `bedrooms`                  | Number of bedrooms                      |
| `bathrooms`                 | Number of bathrooms                     |
| `stories`                   | Number of stories/floors                |
| `mainroad`                  | Access to main road (binary: 1 = Yes) |
| `guestroom`                 | Guest room availability (binary)       |
| `basement`                  | Presence of basement (binary)           |
| `hotwaterheating`           | Hot water heating availability (binary)|
| `airconditioning`           | Air conditioning availability (binary) |
| `parking`                   | Number of parking spaces                |
| `prefarea`                  | Preferred area (binary)                  |
| `furnishingstatus_semi-furnished` | One-hot encoded furnishing status  |
| `furnishingstatus_unfurnished`     | One-hot encoded furnishing status  |

> Furnishing status uses one-hot encoding with three categories:  
> - Furnished (0, 0)  
> - Semi-Furnished (1, 0)  
> - Unfurnished (0, 1)  

---

## 📊 Data Exploration & Visualization

- **Matplotlib & Seaborn** are used to perform exploratory data analysis (EDA).
- Visualized correlations between features and the target price.
- Distribution plots and pairplots help understand feature relationships.
- Insights from visualization guide feature selection and model building.

Example visualizations include:

- Scatter plots of price vs area
- Boxplots of price distribution by furnishing status
- Heatmaps of feature correlation matrix

---

📁 Project Structure
House-Price-Prediction-ML/
 app.py                      # Streamlit app frontend
 house_price_prediction.py   # Model training and evaluation script
 model.pkl                   # Saved trained model file
 data/
 ouse_data.csv          # Dataset CSV file
 .gitignore
 requirements.txt            # Python dependencies
 README.md                   # Project documentation


 # 🏠 How to Run the House Price Prediction App

This guide will walk you through the steps to **set up**, **install dependencies**, and **run** the House Price Prediction web app built with Python and Streamlit.

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- ✅ Python 3.8 or higher
- ✅ Git (optional, if cloning repo)
- ✅ pip (Python package manager)

---

 1. Clone or Download the Project

If you haven't already:

git clone https://github.com/Rupakverse/House-Price-Prediction-ML.git
cd House-Price-Prediction-ML
 
 2. Set Up a Virtual Environment (Recommended)
 python -m venv .venv
Activate the virtual environment:.\.venv\scripts\activate

3. Install Dependencies
If you have a requirements.txt:

pip install -r requirements.txt

4. Train the Model (If Not Already Trained)
Run this to train and save the model as model.pkl:

python house_price_prediction.py

5. run the streamlit app
Now launch the web interface:
streamlit run app.py
This will open the app in your default web browser.

6. Deactivate Virtual Environment (When Done)
deactivate




Author
Rupak Lamichhane
📧 rupaklamichhane09@gmail.com
🔗 LinkedIn
💻 GitHub

Acknowledgements
Thanks to open-source Python libraries and the data sources that made this project possible.

Feel free to open issues or submit pull requests to improve the project!
