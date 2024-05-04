from flask import Flask, request

app = Flask(__name__) 

@app.route('/registroEstudiante')
def registro():
    return 'Registro Estudiantesss'

if __name__ == '__main__':
    app.run(debug=True)