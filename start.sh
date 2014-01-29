#!/bin/bash
uwsgi --socket :9000 --wsgi-file colegio/wsgi.py -d logfile.log


