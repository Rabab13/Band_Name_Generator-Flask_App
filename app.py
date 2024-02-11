from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        street = request.form['street']
        band_name = request.form['band_name']
        pet = request.form['pet']
        band_name_generated = street + ' ' + band_name + ' ' + pet
        return render_template('index.html', band_name_generated=band_name_generated, pet=pet)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)