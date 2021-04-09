from src import app
from src.cleaner import Cleaner
from src.geocode import Geocoder

@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()