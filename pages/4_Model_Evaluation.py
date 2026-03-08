import streamlit as st
import matplotlib.pyplot as plt

st.title("Model Evaluation")

accuracy = [0.65,0.72,0.80,0.86]
val_accuracy = [0.60,0.70,0.78,0.84]

fig, ax = plt.subplots()

ax.plot(accuracy,label="Train Accuracy")
ax.plot(val_accuracy,label="Validation Accuracy")

ax.legend()

st.pyplot(fig)

st.write("Final Accuracy: 86%")
