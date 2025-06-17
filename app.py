
import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

# Numerical Inputs
area = st.number_input("Area (in sq ft)", min_value=100)
bedrooms = st.slider("Number of Bedrooms", 1, 10)
bathrooms = st.slider("Number of Bathrooms", 1, 10)
stories = st.slider("Number of Stories", 1, 4)
parking = st.slider("Parking Spaces", 0, 5)

# Binary Inputs
mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

# Furnishing Status: One-Hot Encoding
furnishingstatus = st.selectbox("Furnishing Status", ["Furnished", "Semi-Furnished", "Unfurnished"])
fs_semi = 1 if furnishingstatus == "Semi-Furnished" else 0
fs_unfurnished = 1 if furnishingstatus == "Unfurnished" else 0

# Convert Yes/No to 1/0
def yn(val): return 1 if val == "Yes" else 0

# Prepare input
input_data = np.array([[
    area,
    bedrooms,
    bathrooms,
    stories,
    yn(mainroad),
    yn(guestroom),
    yn(basement),
    yn(hotwaterheating),
    yn(airconditioning),
    parking,
    yn(prefarea),
    fs_semi,
    fs_unfurnished
]])

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏷️ Estimated House Price: ₹ {prediction:,.2f}")
