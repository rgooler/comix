#!/bin/bash
rm -rf virtualenv
virtualenv virtualenv
virtualenv/bin/pip install flask==0.10.1
virtualenv/bin/pip install natsort==3.2.0
virtualenv/bin/pip install uwsgi
