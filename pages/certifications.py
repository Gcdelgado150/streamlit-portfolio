import streamlit as st
from streamlit_extras.grid import grid 
import pandas as pd

st.set_page_config(page_title="Certifications", page_icon=":memo:", layout="wide")
st.markdown("# Certifications")

df = pd.read_csv("../streamlit-portfolio/data/certifications.csv")

# Custom CSS
st.markdown("""
    <style>
    .certificate-container {
        background-color: #333333;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 10px;
    }
    .certificate-title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    .certificate-details {
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

for i, cert in df.iterrows():
    with st.expander(cert["Certificate"]):
        print(cert['Link'])
        if cert['Link'] != None:
            st.markdown(f"""
                <div class="certificate-container">
                    <div class="certificate-title">{cert["Certificate"]}</div>
                    <div class="certificate-details">
                        <p>Issued on: {cert["Issue_date"]}</p>
                        <p>Issuer: {cert["Issuer"]}</p>
                        <p><a class="certificate-link" href="{cert['Link']}" target="_blank">View Certificate</a></p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="certificate-container">
                    <div class="certificate-title">{cert["Certificate"]}</div>
                    <div class="certificate-details">
                        <p>Issued on: {cert["Issue_date"]}</p>
                        <p>Issuer: {cert["Issuer"]}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            