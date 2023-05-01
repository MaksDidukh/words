from flask import Flask, request, jsonify ,render_template
from text_get import *
app = Flask(__name__)

@app.route('/get_words', methods=['POST'])
def get_words():
    with open('data_ru.txt', 'r') as f:
        words = f.read().split()

    predicted_words = random.sample(words, 20)

    return jsonify(predicted_words=predicted_words)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def test():
    return render_template('test.html')
@app.route('/ru', methods=['POST'])
def predict():
    file_path = 'data_ru.txt'  # Путь к файлу с текстом
    input_word = request.form['input_word']
    words = load_text_file(file_path)
    predicted_words = predict_next_words(words, input_word)
    return jsonify(predicted_words=predicted_words)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
