import streamlit as st
import pandas as pd

st.title("🏦 Model Monitoring Dashboard")

psi = 0.18
ks = 0.32
auc = 0.78

st.metric("PSI", psi)
st.metric("KS", ks)
st.metric("AUC", auc)

try:
    csi_df = pd.read_csv("../data/csi.csv")
    st.dataframe(csi_df)
except:
    st.write("CSI data not found")
