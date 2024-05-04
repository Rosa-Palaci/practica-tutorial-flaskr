from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/registroEstudiante')
def registro():
    return render_template('registroEstudiantes.html')

if __name__ == '__main__':
    app.run(debug=True)