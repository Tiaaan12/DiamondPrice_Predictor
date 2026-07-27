import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model/linear_regress_diamond.pkl")

st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="wide"
)

st.markdown("""
<style>
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}
</style>
""", unsafe_allow_html=True)
title_col, result_col = st.columns([3, 2])

with title_col:
    st.title("💎 Diamond Price Prediction System")
    st.write("Predict the price of a diamond using **Linear Regression**.")

with result_col:
    result_placeholder = st.empty()

st.divider()

col1, col2 = st.columns(2)

with col1:

    carat = st.number_input(
        "Carat",
        min_value=0.10,
        max_value=5.50,
        value=1.00,
        step=0.01
    )

    cut = st.selectbox(
        "Cut",
        ["Fair", "Good", "Very Good", "Premium", "Ideal"]
    )

    color = st.selectbox(
        "Color",
        ["D", "E", "F", "G", "H", "I", "J"]
    )

    clarity = st.selectbox(
        "Clarity",
        ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    )

with col2:

    depth = st.number_input(
        "Depth",
        value=61.5
    )

    table = st.number_input(
        "Table",
        value=57.0
    )

    x = st.number_input(
        "Length (x)",
        value=5.50
    )

    y = st.number_input(
        "Width (y)",
        value=5.50
    )

    z = st.number_input(
        "Depth (z)",
        value=3.40
    )

if st.button("💎 Predict Price", use_container_width=True):

    sample = pd.DataFrame({

        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]

    })

    log_prediction = model.predict(sample)[0]
    prediction = np.expm1(log_prediction)

    result_placeholder.markdown(
    f"""
    <h2 style="margin-top:20px;">
        💎 Estimated Diamond Price:
        <span style="color:#1f77b4;">${prediction:,.2f}</span>
    </h2>
    """,
    unsafe_allow_html=True
)