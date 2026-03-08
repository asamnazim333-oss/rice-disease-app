import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Model Evaluation")

st.write("### Model Metrics (Demo)")

accuracy = 0.89
loss = 0.28

st.metric("Accuracy", f"{accuracy * 100:.2f}%")
st.metric("Loss", loss)

st.write("### Training vs Validation Accuracy (Demo)")

train_acc = [0.70, 0.78, 0.84, 0.89]
val_acc = [0.68, 0.75, 0.83, 0.87]

fig, ax = plt.subplots()
ax.plot(train_acc, label="Train Accuracy")
ax.plot(val_acc, label="Validation Accuracy")
st.pyplot(fig)
st.write("Final Accuracy: 86%")


st.write("### Confusion Matrix (Demo)")

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

classes = [
"Healthy",
"Bacterial_Leaf_Blight",
"Leaf_Blast",
"Brown_Spot"
]

matrix = np.array([
[50,2,1,0],
[3,45,2,1],
[1,3,47,2],
[0,1,2,48]
])

fig, ax = plt.subplots()

ax.imshow(matrix)

ax.set_xticks(range(len(classes)))
ax.set_yticks(range(len(classes)))

ax.set_xticklabels(classes,rotation=45)
ax.set_yticklabels(classes)

st.pyplot(fig)


st.write("""  
✔ Confusion matrix values are sample only.
""")
