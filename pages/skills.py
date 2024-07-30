import streamlit as st
from streamlit_extras.grid import grid 
import json

st.markdown("# Skills")
st.sidebar.markdown("# Skills")

with open("../streamlit-portfolio/data/skill_tree.json", "r") as f:
    skills_tree = json.load(f)

skills_tree = dict(sorted(skills_tree.items(), key=lambda kv: kv[1], reverse=True))

cols = st.columns(4)

with cols[-1]:
    for skill, value in skills_tree.items():
        bar = st.progress(value=value *20, text=f"Skill {skill}:")