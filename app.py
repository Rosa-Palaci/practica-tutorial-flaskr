from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola Mundo'

@app.route('/registroEstudiante')
def registro():
    return 'Registro Estudiante'