from flask import Flask, render_template, request, redirect, url_for
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        precipitation = float(request.form['precipitation'])
        temp_max = float(request.form['temp_max'])
        temp_min = float(request.form['temp_min'])
        wind = float(request.form['wind'])
        
        # Load the model
        model = pickle.load(open('weather.pkl', 'rb'))
        
        # Make prediction
        prediction = model.predict([[precipitation, temp_max, temp_min, wind]])[0]
        
        # Map prediction to weather type
        weather_dict = {
            1: 'rain',
            2: 'sun',
            3: 'fog',
            4: 'drizzle',
            5: 'snow'
        }
        
        crop = weather_dict.get(int(prediction), 'Unknown')
        
        return render_template('result.html', crop=crop)

if __name__ == '__main__':
    app.run(debug=True)
