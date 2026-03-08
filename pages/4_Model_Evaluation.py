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

st.write("### Confusion Matrix (Demo)")

matrix = [
    [48, 2, 1, 1],
    [3, 45, 2, 0],
    [1, 4, 46, 3],
    [2, 1, 3, 44]
]

fig2, ax2 = plt.subplots()
ax2.imshow(matrix)
st.pyplot(fig2)

st.write("""  
✔ Confusion matrix values are sample only.
""")
