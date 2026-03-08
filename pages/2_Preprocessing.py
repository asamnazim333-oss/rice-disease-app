import streamlit as st
import numpy as np
from PIL import Image

st.title("Image Preprocessing")

file = st.file_uploader("Upload rice leaf image")

if file:

    img = Image.open(file)

    st.image(img, caption="Original Image")

    img = img.resize((224,224))

    st.image(img, caption="Resized Image")

    img = np.array(img)/255.0

    st.write("Normalized shape:",img.shape)
