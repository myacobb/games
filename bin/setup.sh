#!/bin/bash

# Mac OS
brew install python-tk@3.9

# Ubuntu
# sudo apt-get install python3-tk

pip3 install virtualenv
python3 -m virtualenv env
 
# activate environment
source "env/bin/activate"
# install dependencies
pip3 install -r requirements.txt
# deactivate environment
deactivate