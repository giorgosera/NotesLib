###################################
# Fab file to deploy these app    #
# to various servers.             #
# Author: Giorgos Eracleous       #
###################################

import os
from fabric.api import *
from fabric.colors import green

APP_NAME = "noteslib"

####################
# PROCESS COMMANDS #
####################

def start():
    '''
    Starts the server.
    '''
    local("python app.py")
    print(green("Server started!"))
