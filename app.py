import requests
from flask import Flask, render_template, request, redirect, url_for
from models import SubmissionModel
from utils import save_to_json

app = Flask(__name__)
submission_model = SubmissionModel()

def get_weather(city=''):
    api_key = '938a17cf1fbd4f4997d110440242509' 
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        return (weather_data['current']['condition']['text'], 
                weather_data['current']['temp_c'])
    
    return "Unavailable", "Unavailable"

@app.route('/')
def index():
    submissions = submission_model.get_submissions()
    return render_template('index.html', submissions=submissions)

@app.route('/submit', methods=['POST'])
def submit_form():
    submission_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'city': request.form['city']
    }
    
    weather_description, temperature = get_weather(submission_data['city'])
    submission_data['weather'] = f"{weather_description} at {temperature}°C"
    
    submission_model.save_submission(submission_data)
    save_to_json(submission_data)
    
    return redirect(url_for('index'))

@app.route('/submissions', methods=['GET'])
def show_submissions():
    submissions = submission_model.get_submissions()
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
