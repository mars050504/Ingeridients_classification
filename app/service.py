import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
from PIL import Image
from app.model import class_mapping, ingredients_mapping

# load model
print("loading model")
model = load_model("./model.h5")
print("model loaded successfully")

# allowed file extension
ALLOWED_EXT = set(["jpg", "jpeg", "png"])
def not_allowed(filename):
  return "." in filename and filename.rsplit('.', 1)[1] not in ALLOWED_EXT

# read image from request
def read_image(file):
  # Open the image file
  image = Image.open(file).convert("RGB") # convert to RGB if neccessary
  image = image.resize((150, 150)) # resize to the model's expected input size
  
  # Preprocess the image
  image_array = np.array(image, dtype=np.float32) / 255.0  # Normalize pixel values
  image_tensor = np.expand_dims(image_array, axis=0)  # Add batch dimension
  
  return image_tensor

def predict_image(image_tensor):
  # perform prediction
  predictions = model.predict(image_tensor)
  
  # recognize the class
  result = np.array(predictions[0])
  class_name = class_mapping[result.argmax()]
  return ingredients_mapping[class_name]