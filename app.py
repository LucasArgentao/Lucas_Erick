import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  Genero = request.form['Genero']
  Casado = request.form['Casado']
  Dependentes = request.form['Dependentes']
  MesesComoCliente = request.form['MesesComoCliente']
  ServicoTelefone = request.form['ServicoTelefone']
  ServicoInternet = request.form['ServicoInternet']
  ServicoSegurancaOnline = request.form['ServicoSegurancaOnline']
  ServicoBackupOnline = request.form['ServicoBackupOnline']
  ProtecaoEquipamento = request.form['ProtecaoEquipamento']
  ServicoSuporteTecnico = request.form['ServicoSuporteTecnico']
  ServicoStreamingTV = request.form['ServicoStreamingTV']
  ServicoFilmes = request.form['ServicoFilmes']
  TipoContrato = request.form['TipoContrato']
  FaturaDigital = request.form['FaturaDigital']
  FormaPagamento = request.form['FormaPagamento']
  ValorMensal = request.form['ValorMensal']
 


  predicao = model.predict([Genero,Casado,Dependentes,MesesComoCliente,
  ServicoTelefone,ServicoInternet,ServicoSegurancaOnline,
  ServicoBackupOnline,ProtecaoEquipamento,ServicoSuporteTecnico,
  ServicoStreamingTV,ServicoFilmes,TipoContrato,FaturaDigital,
  FormaPagamento,ValorMensal])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# c (instala as bibliotecas)
# python app.py (para executar)
# git add .
# git commit -m "nomenovo"
# git push


