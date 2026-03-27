from flask import Flask, jsonify
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

produtos = [
    {'id': 1, 'nome': 'notebook', 'preco': 2500.0},
    {'id': 2, 'nome': 'Mouse', 'preco': 120.0},
    {'id': 3, 'nome': 'Teclado', 'preco': 100.0}
]

cadastro = [
    {'id': 1, 'nome': 'Emerson', 'nota': 8.0},
    {'id': 2, 'nome': 'Leila', 'nota': 8.2},
    {'id': 3, 'nome': 'Livia', 'nota': 9.4}
]

# Rota Principal
@app.route('/')
def root():
    return jsonify({'mensagem': 'API Funcionando!'})

@app.route('/produtos')
def listar_produtos():
    return jsonify(produtos)

@app.route('/cadastro')
def listar_cadastro():
    return jsonify(cadastro)

if __name__ == '__main__':
    app.run()