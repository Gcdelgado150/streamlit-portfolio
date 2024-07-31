import streamlit as st
from streamlit_extras.grid import grid 
import json
import time

def wait_spinner(t):
    def decorator(func):
        def wrapper_func(*args, **kwargs):
            with st.spinner('Wait for it...'):
                time.sleep(t)
            return func(*args, **kwargs)
        return wrapper_func
    return decorator

@wait_spinner(t=1.2)
def retrive_details(skill):
    if skills_tree[skill] == 5:
        st.write(f"{skill} is a solid 5/5!")
        st.write(f"I probably know a lot about {skill}!")
        st.write(f"I've either worked or studied a lot with {skill}!")
        st.write(f"If you ask me to do anything using {skill}, I can probably do it fairly quickly!")
    if skills_tree[skill] == 4:
        st.write(f"{skill} is a very good 4/5!")
        st.write(f"I probably know a lot about {skill}!")
        st.write(f"I've either worked or studied with {skill} a good amount!")
        st.write(f"Still have knowledge to adquired about {skill}, but I would learn them quickly")
    if skills_tree[skill] == 3:
        st.write(f"{skill} is a good 3/5!")
        st.write(f"I probably know about {skill}!")
        st.write(f"I've either worked or studied a bit of {skill}!")
        st.write(f"If you ask me to do anything using {skill}, i can probably do it fairly quickly!")
    if skills_tree[skill] == 2:
        st.write(f"{skill} is a weak 2/5!")
        st.write(f"I probably know a lot about {skill}!")
        st.write(f"I've either worked a lot or studied a lot with {skill}!")
        st.write(f"If you ask me to do anything using {skill}, i can probably do it fairly quickly!")
    if skills_tree[skill] == 1:
        st.write(f"{skill} is a bad 2/5!")
        st.write(f"I've heard about {skill}!")
        st.write(f"Probably had contact once with {skill} but still has a lot of room for improvement!")

st.set_page_config(page_title="Skills", page_icon=":memo:", layout="wide")
st.markdown("# Skills")

with open("../streamlit-portfolio/data/skill_tree.json", "r") as f:
    skills_tree = json.load(f)

skills_tree = dict(sorted(skills_tree.items(), key=lambda kv: kv[1], reverse=True))

cols = st.columns([3, 1])  # 75% and 25% layout

placeholder = "All skilss!"
# First column (75% width)
with cols[0]:
    st.write("In this page I showcase my top skills, in order of expertise!")
    st.divider()
    option = st.selectbox(label="You can also select an specific skills to see details!",
                 options=[placeholder] + list(skills_tree.keys()),
                 placeholder=placeholder)
    st.divider()

    if option != placeholder:
        st.write(f"Ok, let met get details from this skill: {option}")
        retrive_details(skill=option)

# Second column (25% width) with progress bars
with cols[1]:
    for skill, value in skills_tree.items():
        if option == placeholder: 
            st.progress(value=value * 20, text=f"Skill {skill}:")
        else:
            if skill == option:
                st.progress(value=value * 20, text=f"Skill {skill}:")