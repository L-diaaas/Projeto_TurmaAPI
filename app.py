from flask import Flask, jsonify, request
import dici

app = Flask(__name__)

@app.route('/alunos',methods=['POST'])
def createAluno():
    dados = request.json
    dici['alunos'].append(dados)
    return jsonify(dados)

@app.route('/alunos', methods=["GET"])
def getAlunos():
    dados=dici['alunos']
    return jsonify(dados)

@app.route("/alunos/<int:idAluno>", methods=['GET'])
def getAlunosID(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
            dados = request.json
            return jsonify(dados)
        else:
            return jsonify("aluno nao encontrado")

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
            dados = request.json
            aluno["id"] = dados['id']
            aluno['nome'] = dados['nome']

            return jsonify(dados)
        else:
            return jsonify("aluno nao encontrado")


@meuApp.route('/alunos', methods=['DELETE'])
def delete_alunos():
    return jsonify('mensagem': 'Todos os Alunos foram removidos.')


@meuApp.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_alunosID(idAluno):
    for aluno in alunos:
        if aluno['id'] == idAluno:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

if __name__=="__main__":
    app.run(debug=True)