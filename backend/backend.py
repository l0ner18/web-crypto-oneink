from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/alghoritm-yash', methods=['POST'])
def alghoritm_yash():
    try:
        json_data = request.get_json()

        key = json_data.get('key')
        message = json_data.get('message')

        if key is None or message is None:
            return jsonify({'error': 'Неверный формат JSON. Отсутствуют key или data.'}), 400

        result = subprocess.run(['python', 'alghoritm-yash.py', key, message], capture_output=True, text=True)

        return jsonify({'result': result.stdout.strip()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


@app.route('/alghoritm-sdes', methods=['POST'])
def alghoritm_sdes():
    try:
        json_data = request.get_json()

        key = json_data.get('key')
        message = json_data.get('message')

        if key is None or message is None:
            return jsonify({'error': 'Неверный формат JSON. Отсутствуют key или data.'}), 400

        result = subprocess.run(['python', 'alghoritm-sdes.py', key, message], capture_output=True, text=True)

        return jsonify({'result': result.stdout.strip()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


@app.route('/alghoritm-saes', methods=['POST'])
def alghoritm_saes():
    try:
        json_data = request.get_json()

        key = json_data.get('key')
        message = json_data.get('message')

        if key is None or message is None:
            return jsonify({'error': 'Неверный формат JSON. Отсутствуют key или data.'}), 400

        result = subprocess.run(['python', 'alghoritm-saes.py', key, message], capture_output=True, text=True)

        return jsonify({'result': result.stdout.strip()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)