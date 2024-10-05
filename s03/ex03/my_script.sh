#!/bin/bash
VENV_DIR="local_lib"

python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate
# pip install -r requirement.txt