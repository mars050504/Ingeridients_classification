import os

from flask import Blueprint, request
from app.dto import create_response
from app.service import not_allowed, read_image, predict_image

api = Blueprint("api", __name__)

@api.route('/ping', methods=['GET'])
def ping():
  """
  Ping the server to check if it is running
  ---
  responses:
    200:
      description: Server running
      examples:
        application/json: {'status': 'success', 'message': 'server running', 'data': null}
  """
  return create_response(status="success", message="server running",)

# main route
@api.route('/predict', methods=['POST'])
def predict():
  """
  Predict the class of an image
  ---
  parameters:
    - name: input_image
      in: formData
      type: file
      required: true
      description: The image to be predicted
  responses:
    200:
      description: Image predicted successfully
      examples:
        application/json: {'status': 'success', 'message': 'image predicted successfully', 'data': [
      {
        "recipe_name": "Tomato Soup",
        "ingredients": [
          "2 ripe tomatoes",
          "1 onion",
          "2 garlic cloves",
          "1 cup vegetable broth",
          "Salt and pepper to taste",
          "1 tablespoon olive oil"
        ],
        "instructions": [
          "Heat olive oil in a pot and sauté chopped onion and garlic until soft.",
          "Add chopped tomatoes and cook for 5 minutes.",
          "Add vegetable broth and bring to a boil.",
          "Simmer for 10 minutes and season with salt and pepper.",
          "Blend the soup until smooth and serve hot."
        ]
      },
      {
        "recipe_name": "Tomato Salad",
        "ingredients": [
          "3 tomatoes",
          "1 cucumber",
          "1 tablespoon olive oil",
          "1 teaspoon lemon juice",
          "Salt and pepper to taste",
          "Fresh basil leaves"
        ],
        "instructions": [
          "Chop tomatoes and cucumber into bite-sized pieces.",
          "Toss the vegetables with olive oil and lemon juice.",
          "Season with salt, pepper, and fresh basil leaves.",
          "Serve chilled as a refreshing salad."
        ]
      }
    ]}
    400:
      description: Invalid image
      examples:
        application/json: {'status': 'error', 'message': 'input image invalid'}
    500:
      description: Internal server error
      examples:
        application/json: {'status': 'error', 'message': 'internal server error'}
  """
  
  if 'input_image' not in request.files:
    return create_response(message="input image invalid", status="error", status_code=400)
  
  file = request.files['input_image']
  if file.filename == '' or not_allowed(file.filename):
    return create_response(message="input image invalid", status="error", status_code=400)
  
  try:
    # read image
    image_tensor = read_image(file)
    
    # predict image
    recipe_response = predict_image(image_tensor)
    
    return create_response(data=recipe_response, status="success", message="image predicted successfully")
  
  except Exception as e:
    print("error : " + str(e))
    return create_response(message="internal server error", status="error", status_code=500)