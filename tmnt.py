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
    elif ninja_color == 'red':
        return render_template('raph.html')
    elif ninja_color == 'purple':
        return render_template('don.html')
    else:
        return render_template('not.html')


app.run(debug=True)
