#!/usr/bin/env python3
# Author: Johnny C
# File:   jc_app.py
# Descr:  Simple python3 main() app with logging to stdio and rotating log file (by default)
#     :   %s/XXX/YourAppName/g and you will automatically check for _LOGDIR and _LOGLEVEL while choosing sane defaults if unset
import os
import sys
import datetime
import logging

from pathlib  import Path
from datetime import datetime
from logging import FileHandler, StreamHandler
from logging import info, debug
def setup_XXX_Logging(curr_log_file, curr_log_level):
    """Will attempt to reference ENV.XXX_LOGLEVEL before falling back to INFO"""
    console_formatter = logging.Formatter('%(filename)s: %(funcName)s:   %(message)s  ' )
    file_formatter = console_formatter # keep these the same for now
 
    stream_handler = StreamHandler() #This will hook up STDIO
    stream_handler.setFormatter(console_formatter) # STDIO gets a more terse output

    file_handler = FileHandler(curr_log_file, mode="a")
    file_handler.setFormatter(file_formatter)
    
    ##jc: I feel like this belongs somewhere else, but here it lives for now..
    appLogger = logging.getLogger() #This is often refered to as the 'root' logger
    appLogger.setLevel(curr_log_level) 

    appLogger.addHandler(stream_handler) 
    appLogger.addHandler(file_handler)
    return appLogger

def get_XXX_log_fname_level():
    """Will attempt to refernce ENV.XXX_LOG before falling back to CWD."""
    try:
        p = os.environ['XXX_LOGDIR']
    except Exception:
        p =Path.cwd()
    path = Path(p)


    #curr_fname = "XXX_LOG-" + datetime.today().strftime('%Y_%m_%d_%H%M') + ".log"
    curr_fname = "XXX_LOG-" + "curr" + ".log"
    
    curr_file = path / curr_fname
    curr_log_level = os.environ.get("XXX_LOGLEVEL", "DEBUG")
    return (curr_file, curr_log_level)


def prepare_lib_usb():
    """ Check to see that we have permissions etc to enumerate devices with libusb"""
    debug("Preparing lib usb..")
if __name__ == "__main__":
    curr_log_file, curr_log_level = get_XXX_log_fname_level() 
    print("%s Initialzing logging: Level:%s  file:%s" % (sys.argv[0], curr_log_level, curr_log_file))
    setup_XXX_Logging(curr_log_file, curr_log_level) 
    logging.info("%s logging to %s " % (sys.argv[0], curr_log_file))
    prepare_lib_usb()
