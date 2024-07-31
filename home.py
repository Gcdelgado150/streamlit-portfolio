import streamlit as st
import pandas as pd
import os

# Set page config
st.set_page_config(page_title="Portfolio Gcdelgado", page_icon=":memo:", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            background: #121212;
            color: #e0e0e0;
        }
        header {
            background: #6200ea;
            color: #fff;
            padding: 1em 0;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        .intro {
            text-align: center;
            padding: 2em 0;
        }
        .intro h1 {
            font-size: 2.5em;
            color: #bb86fc;
        }
        .projects {
            display: flex;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            padding: 1em 0;
            scroll-behavior: smooth;
        }
        .project {
            background: #1f1f1f;
            border: 2px solid #bb86fc;
            margin: 0 1em;
            padding: 1em;
            min-width: 300px;
            box-sizing: border-box;
            transition: transform 0.3s, box-shadow 0.3s;
            flex: 0 0 auto;
        }
        .project:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px #bb86fc;
        }
        .project img {
            max-width: 100%;
            border-bottom: 2px solid #bb86fc;
            padding-bottom: 1em;
            margin-bottom: 1em;
        }
        .project h3 {
            margin-top: 0;
            color: #bb86fc;
        }
        .project p {
            color: #e0e0e0;
        }
        .project a {
            display: inline-block;
            margin-top: 1em;
            padding: 0.5em 1em;
            background: #6200ea;
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
            transition: background 0.3s;
        }
        .project a:hover {
            background: #3700b3;
        }
        footer {
            background: #6200ea;
            color: #fff;
            text-align: center;
            padding: 1em 0;
            position: relative;
            width: 100%;
        }
        footer a {
            color: #bb86fc;
            text-decoration: none;
        }
        footer a:hover {
            text-decoration: underline;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 100px; /* Adjust the gap between buttons as needed */
        }
        .button {
            background-color: #f0f0f0;
            border: none;
            color: black;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Header
st.markdown('<header><div class="container"><h1>Guilherme C. Delgado</h1></div></header>', unsafe_allow_html=True)

st.markdown("""
    <div class="button-container">
        <button class="button" onclick="window.location.href='pages/certifications'">Certifications</button>
        <button class="button" onclick="window.location.href='/skills'">Skills</button>
        <button class="button" onclick="window.location.href='/contact'">Contact</button>
    </div>
            """, unsafe_allow_html=True)

st.divider()

# Introduction section
st.markdown("""<div class="container">
            <section class="intro">
            <p>Welcome to my portfolio. <br>
            Here you can find some of the projects 
            I\'ve been working on and the code behind them. 
            Feel free to explore and get in touch if you have any questions or opportunities!</p></section></div>""", 
            unsafe_allow_html=True)

st.divider()

# Styling
st.markdown(
    """
    <style>
    .project {
        width: 300px;
        height: 200px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: center;
    }
    .project h3 {
        font-size: 20px;
        margin-bottom: 5px;
    }
    .project p {
        margin-bottom: 0px;
    }
    .project a {
        margin: 0 auto; /* Center the button horizontally */
        text-decoration: none;
        color: white;
        background-color: #007bff;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .project a:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# https://www.kaggle.com/gnomows/code
projects = pd.read_csv("../streamlit-portfolio/data/projects.csv")
cols = st.columns(len(projects))
for i, row in enumerate(projects.iterrows()):
    with cols[i]:
        st.markdown(
            f"""
            <div class="project">
                <h3>{row[1]["Project"]}</h3>
                <p>{row[1]['Description']}</p>
                <a href="{row[1]['Link']}" target="_blank">View Code</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    '<footer><p>&copy; 2024 Guilherme C. Delgado. All rights reserved.</p><p>Find me on <a href="https://www.linkedin.com/in/guilherme-delgado/" target="_blank">LinkedIn</a></p></footer>', 
    unsafe_allow_html=True
)