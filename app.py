import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pdb  # Import pdb module

# Load the trained model
model = tf.keras.models.load_model('mnist_app.h5')

# Create a Streamlit app
st.title("MNIST Digit Recognition")
st.write("Upload an image of a handwritten digit:")

# Create a file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Create a button to trigger prediction
predict_button = st.button("Predict")

# Define a function to preprocess the image
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    image = np.array(image)  # Convert to numpy array
    image = image.reshape(1, 784)  # Reshape to match input shape
    image = image.astype('float32') / 255  # Normalize
    return image

# Define a function to predict the digit
def predict_digit(image):
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    pdb.set_trace()  # Set a breakpoint
    digit = str(digit)
    digit = int(digit)
    return digit

# Create a text output to display the prediction
prediction_output = st.text("")

# Create a main function to run the app
def main():
    if uploaded_file:
        image = Image.open(uploaded_file)
        preprocessed_image = preprocess_image(image)
        if predict_button:
            digit = predict_digit(preprocessed_image)
            prediction_output.text(f"The predicted digit is: {digit}")

# Run the app
if __name__ == "__main__":
    main()
print("i'm very horny right now")
