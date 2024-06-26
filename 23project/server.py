from weather import get_current_weather
from dotenv import load_dotenv

from flask  import Flask, render_template, request
from waitress import serve
import os
load_dotenv()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    # return "hello"
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    if not bool(city.strip()):
        city = "Goa"
    
    weather_data = get_current_weather(city)
      
    # Check if the response indicates no data found
    if weather_data["cod"] == "404":
        return render_template(
            'city-not-found.html'
        )

    return render_template(
        'weather.html',
        title =weather_data["name"],
        status = weather_data["weather"][0]['description'].capitalize(),
        icon = weather_data["weather"][0]["icon"],
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )

    


if __name__ == "__main__":
    # serve(app, port=os.getenv("PORT", default=8000))
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))