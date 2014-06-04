#!virtualenv/bin/python
from app import app
import config as config

if __name__ == "__main__"
    app.run(port=5000, debug=config.DEBUG, host='0.0.0.0')
