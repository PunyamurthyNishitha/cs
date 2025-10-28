from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own OpenWeatherMap API key
API_KEY = "4eb3703790b356562054106543b748b2"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'].capitalize(),
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather_data = {'error': 'City not found! Please try again.'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
