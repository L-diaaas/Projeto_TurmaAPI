from flask import Flask, jsonify, request

dici = {
    'alunos': [
        {
            'id': 1,
            'nome': 'João',
            'idade': 20,
            'turma_id': 101,
            'data_nasc': '2005-05-15',
            'nota_primeirosem': 7.5,
            'nota_segundosem': 8.0,
            'media_final': 7.75,
        },
    ]
}

app = Flask(__name__)

@app.route('/alunos', methods=['POST'])
def createAluno():
    dados = request.json
    dici['alunos'].append(dados)  
    return jsonify(dados), 201

@app.route('/alunos', methods=["GET"])
def getAlunos():
    dados = dici['alunos']
    return jsonify(dados)

@app.route("/alunos/<int:idAluno>", methods=['GET'])
def getAlunosID(idAluno):
    for aluno in dici["alunos"]:  
        if aluno['id'] == idAluno:
            return jsonify(aluno)  
    return jsonify({"mensagem": "Aluno não encontrado"}), 404  

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    for aluno in dici["alunos"]:  
        if aluno['id'] == idAluno:
            dados = request.json
            aluno.update(dados)  
            return jsonify(aluno)  
    return jsonify({"mensagem": "Aluno não encontrado"}), 404 

@app.route('/alunos', methods=['DELETE'])
def delete_alunos():
    dici['alunos'].clear()  
    return jsonify({'mensagem': 'Todos os Alunos foram removidos.'})

@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_alunosID(idAluno):
    for aluno in dici["alunos"]:  
        if aluno['id'] == idAluno:
            dici['alunos'].remove(aluno)  
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404  

if __name__ == "__main__":
    app.run(debug=True)
