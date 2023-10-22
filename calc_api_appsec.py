from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

calc = Flask(__name__)
CORS(calc)  # Добавляем поддержку CORS

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Обработка ошибок некорректных запросов
@calc.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

@calc.route('/plus', methods=['POST'])
def addition():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

    result = num1 + num2
    logging.info(f"Added {num1} and {num2}, result: {result}")
    return jsonify({'result': result})

@calc.route('/minus', methods=['POST'])

def subtraction():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

    result = num1 - num2
    logging.info(f"Subtracted {num2} from {num1}, result: {result}")
    return jsonify({'result': result})

@calc.route('/multiply', methods=['POST'])
def multiplication():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

    result = num1 * num2
    logging.info(f"Multiplied {num1} by {num2}, result: {result}")
    return jsonify({'result': result})

@calc.route('/divide', methods=['POST'])
def division():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
        logging.info(f"Divided {num1} by {num2}, result: {result}")
        return jsonify({'result': result})

    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    calc.run(host="0.0.0.0", debug=True)
