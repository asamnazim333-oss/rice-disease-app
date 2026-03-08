import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dataset Overview")

classes = ["Healthy","Brown Spot","Leaf Blast"]

data = [500,420,380]

df = pd.DataFrame({
    "Disease":classes,
    "Images":data
})

st.write("Dataset distribution")

fig, ax = plt.subplots()

ax.bar(classes,data)

st.pyplot(fig)

st.markdown("""
### Classes

Healthy  
Brown Spot  
Leaf Blast

These diseases affect rice productivity worldwide.
""")
