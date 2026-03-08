import streamlit as st

st.set_page_config(
    page_title="Rice Disease Detection",
    layout="wide"
)

st.title("🌾 Rice Disease Detection AI")

st.markdown("""
This application detects **rice leaf diseases using Deep Learning**.

Use the sidebar to navigate:

• Dataset Overview  
• Image Preprocessing  
• Disease Classification  
• Model Evaluation
""")
