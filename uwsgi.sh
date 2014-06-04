#!/bin/bash
virtualenv/bin/uwsgi -s uwsgi.sock -w app:app > /var/log/nginx/comics.thisstuffismine.com-flask.log 2>&1
rm uwsgi.sock
