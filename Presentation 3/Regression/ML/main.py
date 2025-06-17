import streamlit as st
import pickle
import numpy as np
import datetime

# Page setup
st.set_page_config(page_title="MPG Predictor", page_icon="🚗")
st.title("🚗 Car MPG Predictor")
st.markdown("### Estimate your car's fuel efficiency (Miles Per Gallon) based on engine and performance specs.")

# Model selection
model_choice = st.selectbox("🔧 Choose Prediction Model", ["Basic MPG Model", "Advanced MPG Model"])
model_path = (
    "Basic_mpg_regression_model.pkl"
    if model_choice == "Basic MPG Model"
    else "Advance_mpg_regression_model.pkl"
)

# Load model
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"❌ Model file not found at path: `{model_path}`")
    st.stop()

# Sidebar for inputs (limited to best current cars)
st.sidebar.header("📥 Enter Car Specifications")

cylinders = st.sidebar.number_input("🔩 Engine Cylinders", min_value=2, max_value=8, step=1)
displacement = st.sidebar.number_input("🧱 Engine Displacement (cc)", min_value=50.0, max_value=250.0, step=0.1)
horsepower = st.sidebar.number_input("🐎 Horsepower (HP)", min_value=40.0, max_value=200.0, step=0.1)
weight = st.sidebar.number_input("⚖️ Vehicle Weight (lbs)", min_value=1500.0, max_value=4000.0, step=1.0)
acceleration = st.sidebar.number_input("🏁 0–60 mph Acceleration (sec)", min_value=2.0, max_value=10.0, step=0.1)

# 📅 Model Year from Calendar (limited to 1970–1999)
import datetime

selected_date = st.sidebar.date_input(
    "📅 Select Production Date",
    value=datetime.date(1980, 1, 1),  # Default date within range
    min_value=datetime.date(1970, 1, 1),
    max_value=datetime.date(1999, 12, 31)
)

model_year = selected_date.year - 1900  # e.g., 1999 → 99



# Engineered features
displacement_on_power = displacement / horsepower if horsepower != 0 else 0
weight_on_cylinder = weight / cylinders if cylinders != 0 else 0
acceleration_on_power = acceleration / horsepower if horsepower != 0 else 0
acceleration_on_cylinder = acceleration / cylinders if cylinders != 0 else 0

# Display inputs
st.subheader("📝 Car Input Summary")
st.write({
    "Cylinders": cylinders,
    "Displacement (cc)": displacement,
    "Horsepower (HP)": horsepower,
    "Weight (lbs)": weight,
    "Acceleration (0-60 sec)": acceleration,
    "Model Year": model_year,
    "Displacement/HP": round(displacement_on_power, 2),
    "Weight/Cylinder": round(weight_on_cylinder, 2),
    "Acceleration/HP": round(acceleration_on_power, 2),
    "Acceleration/Cylinder": round(acceleration_on_cylinder, 2),
})

# Predict
if st.button("🚀 Predict MPG"):
    features = np.array([
        cylinders, displacement, horsepower, weight, acceleration, model_year,
        displacement_on_power, weight_on_cylinder, acceleration_on_power, acceleration_on_cylinder
    ]).reshape(1, -1)

    prediction = model.predict(features)
    mpg = round(prediction[0], 2)

    st.success(f"🏎️ Estimated MPG: **{mpg} miles/gallon**")

    # Extra feedback
    if mpg >= 30:
        st.info("🔥 Excellent fuel efficiency! Perfect for long drives.")
    elif mpg >= 20:
        st.info("⚖️ Good balance of power and economy.")
    else:
        st.warning("⛽ Low efficiency — consider engine tuning or lighter models.")
