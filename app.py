import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Merhaba, Flask Uygulamasına Hoş Geldiniz!</h1>
    <iframe src="/pdf" width="100%" height="100%">
        PDF dosyasını görüntüleyemiyorsanız, <a href="/pdf">buraya tıklayın</a>.
    </iframe>
    '''

@app.route('/pdf')
def show_pdf():
    # PDF dosyasının tam yolunu belirtiyoruz
    return send_file('/app/yivliinsaat.pdf', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
