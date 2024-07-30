import streamlit as st
from helpers.help import decorate_page_name
from streamlit_extras.grid import grid 
import json

with open("/home/gcdelgado/Documents/Projetos/Streamlit/data/skill_tree.json", "r") as f:
    skills_tree = json.load(f)

skills_tree = dict(sorted(skills_tree.items(), key=lambda kv: kv[1], reverse=True))

st.markdown(decorate_page_name("# Skills"))
st.sidebar.markdown(decorate_page_name("# Skills"))

cols = st.columns(4)

with cols[-1]:
    for skill, value in skills_tree.items():
        bar = st.progress(value=value *20, text=f"Skill {skill}:")