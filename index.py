from flask import Flask, render_template

app = Flask(__name__)

help = True

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Sobre-nosotros')
def about():
    return render_template('about.html')


@app.route('/Servicios')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)
