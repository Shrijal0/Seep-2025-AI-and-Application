import streamlit as st
import joblib
import numpy as np

# Load models
baseline_model = joblib.load("ML_PROJECT_CLASSIFICATION_Baseline.pkl")
tuned_model = joblib.load("ML_PROJECT_CLASSIFICATION_DecisionTreeTuned.pkl")
st.title("🍷 Wine Classification App")

# Sidebar inputs
st.sidebar.header("Enter Wine Features")

# Numerical inputs
year = st.sidebar.slider("Year", 1950, 2025, 2015)
num_reviews = st.sidebar.slider("Number of Reviews", 0, 1000, 100)
price = st.sidebar.slider("Price ($)", 1, 500, 50)
body = st.sidebar.slider("Body (1-5)", 1, 5, 3)
acidity = st.sidebar.slider("Acidity (1-5)", 1, 5, 3)
wine_age = st.sidebar.slider("Wine Age (years)", 0, 100, 5)

# Derived features
log_price = np.log1p(price)
log_reviews = np.log1p(num_reviews)

# Categorical options
type_options = [
    "Cabernet Sauvignon", "Chardonnay", "Garnacha", "Mencia", "Merlot",
    "Monastrell", "Other", "Palomino", "Parellada", "Red", "Ribera Del Duero Red",
    "Rioja Red", "Rioja White", "Rose", "Sauvignon Blanc", "Shiraz",
    "Tempranillo", "Toro Red", "Verdejo", "White"
]

region_options = [
    "Campo De Borja", "Castilla La Mancha", "Castilla y Leon", "Catalunya", "Jumilla",
    "Madrid", "Montsant", "Other", "Penedes", "Priorato", "Rias Baixas",
    "Ribera del Duero", "Rioja", "Sardon de Duero", "Toro", "Vino de Espana"
]

# Categorical inputs
wine_type = st.sidebar.selectbox("Wine Type", type_options)
region = st.sidebar.selectbox("Region", region_options)

# One-hot encoding
type_encoded = [1 if t == wine_type else 0 for t in type_options]
region_encoded = [1 if r == region else 0 for r in region_options]

# Final feature list (excluding raw price)
features = [
    year, num_reviews, body, acidity, wine_age,
    log_price, log_reviews
] + type_encoded + region_encoded

features = np.array(features).reshape(1, -1)

# Prediction
if st.button("Predict"):
    baseline_prediction = baseline_model.predict(features)[0]
    tuned_prediction = tuned_model.predict(features)[0]

    st.success(f"🧠 Baseline Model Prediction: **{baseline_prediction}**")
    st.success(f"✨ Tuned Model Prediction: **{tuned_prediction}**")
