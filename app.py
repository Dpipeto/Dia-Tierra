from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('memoria_preescolar_3ro.html')

@app.route('/memoria_3ro_5to.html/')
def tercero_quinto():
    return render_template('memoria_3ro_5to.html')