from flask import jsonify

def create_response(data=None, message="", status="success", status_code=200):
  response = {
    "status": status,
    "message": message,
    "data": data
  }
  
  return jsonify(response), status_code