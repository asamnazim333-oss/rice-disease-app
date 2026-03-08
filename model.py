import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import numpy as np

CLASS_NAMES = ["Healthy", "Brown Spot", "Leaf Blast"]

def load_model():

    base_model = ResNet50(
        weights="imagenet",
        include_top=False,
        input_shape=(224,224,3)
    )

    x = base_model.output
    x = GlobalAveragePooling2D()(x)

    predictions = Dense(3, activation="softmax")(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    return model


def predict(model, img):

    img = np.expand_dims(img, axis=0)

    predictions = model.predict(img)

    class_index = np.argmax(predictions)

    confidence = predictions[0][class_index]

    return CLASS_NAMES[class_index], confidence
