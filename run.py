#!virtualenv/bin/python
from app import app
import config as config

app.run(port=5000, debug=config.DEBUG)