from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Merhaba, Flask Uygulamasına Hoş Geldiniz!</h1>
    <iframe src="/static/document.pdf" width="100%" height="600px">
        Bu sayfada PDF dosyasını görüntüleyemiyorsanız, <a href="/static/document.pdf">buraya tıklayın</a>.
    </iframe>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
