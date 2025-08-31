from flask import Flask, request, jsonify

app = Flask(__name__)


users = []
current_id = 1 


@app.route('/users', methods=['POST'])
def create_user():
    global current_id
    data = request.json

    if not data or "nome" not in data or "email" not in data:
        return jsonify({"error": "Dados inválidos. Informe nome e email."}), 400

    new_user = {
        "id": current_id,
        "nome": data["nome"],
        "email": data["email"]
    }
    users.append(new_user)
    current_id += 1

    return jsonify(new_user), 201


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado"}), 404


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            if "nome" in data:
                user["nome"] = data["nome"]
            if "email" in data:
                user["email"] = data["email"]
            return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado"}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "Usuário excluído com sucesso"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
