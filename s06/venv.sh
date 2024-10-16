#!/bin/bash
DIR=django_venv
virtualenv $DIR --always-copy
source $DIR/bin/activate
pip install -r requirements.txt