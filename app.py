import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("linear_regress_diamond.pkl")

st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="wide"
)


