from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def ninjaColor(ninja_color):
    if ninja_color == 'blue':
        return render_template('leo.html')
    elif ninja_color == 'orange':
        return render_template('mich.html')


app.run(debug=True)
