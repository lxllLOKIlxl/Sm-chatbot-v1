from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()

    # Проста логіка відповіді
    if 'привіт' in user_message:
        reply = 'Привіт! Чим можу допомогти?'
    elif 'акаунт' in user_message:
        reply = 'Щоб створити акаунт, перейдіть до розділу "Реєстрація".'
    elif 'розклад' in user_message:
        reply = 'Розклад доступний у PDF-файлі. Хочеш, я можу витягнути пари з нього.'
    else:
        reply = 'Не можу відповісти. Спробуйте інакше.'

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(port=5000)

