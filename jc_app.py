#!/usr/bin/env python3
# Author: Johnny C
# File:   jc_app.py
# Descr:  Simple python3 main() app with logging to stdio and rotating log file (by default)
#     :   %s/XXX_App/YourAppName/g and you will automatically check for _LOGDIR and _LOGLEVEL while choosing sane defaults if unset
import os
import sys
import datetime
import logging

from pathlib  import Path
from datetime import datetime
from logging.handlers import WatchedFileHandler
from logging import StreamHandler
def setup_XXX_App_Logging(curr_log_file):
	"""Will attempt to reference ENV.XXX_App_LOGLEVEL before falling back to INFO"""
	simple_formatter = logging.Formatter(logging.BASIC_FORMAT)

	stream_handler = StreamHandler() #This will hook up STDIO
	stream_handler.setFormatter(simple_formatter)

	file_handler = WatchedFileHandler(curr_log_file)
	file_handler.setFormatter(simple_formatter)
	
	##jc: I feel like this belongs somewhere else, but here it lives for now..
	appLogger = logging.getLogger() #This is often refered to as the 'root' logger
	appLogger.setLevel(os.environ.get("XXX_App_LOGLEVEL", "INFO")) #falls back to info
	
	appLogger.addHandler(stream_handler) 
	appLogger.addHandler(file_handler)
	return appLogger

def get_XXX_App_log_fname():
	"""Will attempt to refernce ENV.XXX_App_LOG before falling back to CWD."""
	try:
		p = os.environ['XXX_App_LOGDIR']
	except Exception:
		p =Path.cwd()
	p = Path(p)
	curr_fname = "XXX_App_LOG-" + datetime.today().strftime('%Y_%m_%d_%H%M') + ".log"
	curr_file = p / curr_fname
	return curr_file



if __name__ == "__main__":
	curr_log_file = get_XXX_App_log_fname() 
	setup_XXX_App_Logging(curr_log_file) 
	logging.info("%s logging to %s " % (sys.argv[0], curr_log_file))
