#! /usr/bin/env python
from granpyapp import geocode
from granpyapp import cleaner
from granpyapp.views import app


if __name__ == "__main__":
    app.run(debug=True)
