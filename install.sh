#!/bin/bash

# Create the Git directory if one does not exist
[ -d ${HOME}/Git ] || mkdir ${HOME}/Git
echo "export WORKY_HOME=${HOME}/Git/" >> ${HOME}/.bash_profile

# Create the worky directory for scratch-spaces
[ -d ${HOME}/Worky ] || mkdir ${HOME}/Worky

# Install the python package via setup.py
python setup.py install