from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Caneta", "preco": 2.5},
    {"id": 2, "nome": "Caderno", "preco": 15.0}
]


@app.route('/')
def home():
    return "Olá! Flask está funcionando."


@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify({"mensagem": "Produto adicionado com sucesso!", "produto": novo_produto}), 201

if __name__ == '__main__':
    app.run(debug=True)

