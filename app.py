from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'yivli_insaat_logo_page-0001.jpg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
