from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


todos = [
  { "label": "My first task", "done": False }
]



## GET endpoint
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

## 7.01
# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request_body = request.json
#     print("Incoming request with the following body", request_body)
#     return 'Response for the POST todo'

## 7.02
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)


## 8 DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.remove(todos[position])
    return jsonify(todos), 200

    






# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)