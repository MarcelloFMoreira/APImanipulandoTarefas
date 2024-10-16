from flask import Flask, jsonify, request
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

dados_conexao = (
    "Driver={SQL Server};"
    "Server=MarcelloDRIP;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem-sucedida')

cursor = conexao.cursor()

# Rota para listar todas as tarefas
@app.route('/', methods=['GET'])
def verificar_tarefas():
    listar = """SELECT * FROM Tarefas"""
    cursor.execute(listar)
    tarefas = cursor.fetchall()

    resultado = []
    for linha in tarefas:
        resultado.append({
            'id': linha.id,
            'nome_tarefa': linha.nome_tarefa,
            'stat': linha.stat
        })

    return jsonify(resultado)


# Rota para adicionar uma nova tarefa
@app.route('/', methods=['POST'])
def incluir_tarefa():
    dados = request.json  
    nome = dados.get('nome') 
    nova_tarefa = """INSERT INTO Tarefas(nome_tarefa, stat)
    VALUES (?, 'pendente')"""
    
    cursor.execute(nova_tarefa, (nome,))
    conexao.commit()  

    return jsonify({'message': 'Tarefa adicionada com sucesso!'})

# Rota para remover uma tarefa pelo id
@app.route('/remover/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    verificar = """SELECT * FROM Tarefas WHERE id = ?"""
    cursor.execute(verificar, (id,))
    tarefa = cursor.fetchone()

    if tarefa:
        deletar = """DELETE FROM Tarefas WHERE id = ?"""
        cursor.execute(deletar, (id,))
        conexao.commit()
        return jsonify({'message': f'Tarefa com id {id} removida com sucesso!'})
    else:
        return jsonify({'error': f'Tarefa com id {id} não encontrada!'}), 404

# Rota para marcar uma tarefa como completa
@app.route('/completa/<int:id>', methods=['PUT'])
def completar_tarefa(id):
    verificar = """SELECT * FROM Tarefas WHERE id = ?"""
    cursor.execute(verificar, (id,))
    tarefa = cursor.fetchone()

    if tarefa:
        mudar_status = """UPDATE Tarefas SET stat = 'completa' WHERE id = ?"""
        cursor.execute(mudar_status, (id,))
        conexao.commit()
        return jsonify({'message': f'Tarefa com id {id} marcada como completa!'})
    else:
        return jsonify({'error': f'Tarefa com id {id} não encontrada!'}), 404

# Rota para marcar uma tarefa como pendente
@app.route('/pendente/<int:id>', methods=['PUT'])
def marcar_tarefa_como_pendente(id):
    verificar = """SELECT * FROM Tarefas WHERE id = ?"""
    cursor.execute(verificar, (id,))
    tarefa = cursor.fetchone()

    if tarefa:
        mudar_status = """UPDATE Tarefas SET stat = 'pendente' WHERE id = ?"""
        cursor.execute(mudar_status, (id,))
        conexao.commit()
        return jsonify({'message': f'Tarefa com id {id} marcada como pendente!'})
    else:
        return jsonify({'error': f'Tarefa com id {id} não encontrada!'}), 404


if __name__ == '__main__':
    app.run(debug=True)
