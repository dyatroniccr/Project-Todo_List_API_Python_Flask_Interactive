from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/todos', methods=['GET'])
def todo_get():
    json_text = jsonify(todos)
    return json_text
    #return '<h1>Hello!</h1>'


@app.route('/todos', methods=['POST'])
def add_new_todo():
    #request_body = request.data
    request_body = request.get_json()
    #request_body = request.json
    #decoded_object = json.loads(request_body)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    
    json_text = jsonify(todos)
    #return 'Response for the POST todo'
    #json_text = jsonify({"lista":todos, "message":"ok"})
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    #return 'something'
    
    position = int(position)
    if position >= len(todos):
        return jsonify({"message":"indice invalido"})
    if position < 0:
        return jsonify({"message":"indice invalido"})
    if len(todos) == 0:
        return jsonify({"message":"indice invalido"})
    
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

#python app <=> __main__

# suppose you have your data in the variable some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }



@app.route('/blahblah', methods=['GET'])
def blahblah():
    # you can convert that variable into a json string like this
    #json_text = jsonify(some_data)
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text





# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)