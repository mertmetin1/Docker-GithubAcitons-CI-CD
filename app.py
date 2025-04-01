from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yivli İnşaat</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }

            .container {
                background-color: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
                border-radius: 10px;
                max-width: 900px;
                width: 100%;
            }

            h1 {
                color: #2c3e50;
                font-size: 36px;
                margin-bottom: 20px;
                font-weight: bold;
            }

            img {
                width: 100%;
                max-width: 100%;
                height: auto;
                border-radius: 10px;
            }

            .footer {
                margin-top: 20px;
                color: #7f8c8d;
            }

            a {
                color: #3498db;
                text-decoration: none;
                font-weight: bold;
            }

            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Yivli İnşaat</h1>
            <p>Yakında...</p>
            <img src="/yivliinsaat.jpg" alt="Yivli İnşaat Görseli">
            <div class="footer">
                <p>&copy; 2025 Yivli İnşaat</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/yivliinsaat.jpg')
def show_image():
    return send_file('yivliinsaat.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
