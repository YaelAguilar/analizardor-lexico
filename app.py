from flask import Flask, request, jsonify, render_template
from analyzer import analyze_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    tokens = analyze_text(code)
    token_list = [{'type': tok[0], 'value': tok[1]} for tok in tokens]
    return jsonify(token_list)

if __name__ == '__main__':
    app.run(debug=True)
