import streamlit as st
import numpy as np
from PIL import Image
from model import load_model,predict

st.title("Rice Disease Classification")

model = load_model()

file = st.file_uploader("Upload rice leaf image")

if file:

    img = Image.open(file).resize((224,224))

    st.image(img)

    img = np.array(img)/255.0

    label,confidence = predict(model,img)

    st.success(f"Prediction: {label}")

    st.info(f"Confidence: {confidence*100:.2f}%")
