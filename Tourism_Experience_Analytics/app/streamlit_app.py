import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Tourism Analytics", layout="centered")

st.title("🌍 Tourism Experience Analytics")
st.write("Personalized Attraction Recommendation System")

# Load models
attraction_similarity = joblib.load('../models/attraction_similarity.pkl')
attraction_list = joblib.load('../models/attraction_list.pkl')

# Dropdown
selected_attraction = st.selectbox(
    "Select an attraction you liked:",
    attraction_list
)

# Button
if st.button("Get Recommendations"):
    scores = attraction_similarity[selected_attraction].sort_values(ascending=False)[1:6]

    st.subheader("Recommended Attractions")
    for i, place in enumerate(scores.index, start=1):
        st.write(f"{i}. {place}")
