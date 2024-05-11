from flask import Flask, request, jsonify, render_template
from lexer import lexer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    lexer.input(code)
    tokens = [{'type': tok.type, 'value': tok.value} for tok in lexer]
    return jsonify(tokens)

if __name__ == '__main__':
    app.run(debug=True)
