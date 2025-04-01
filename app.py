from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Merhaba, Flask Uygulamasına Hoş Geldiniz!</h1>
    <img src="/static/yivli_insaat_logo_page-0001.jpg" alt="Image">
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
