import logging
from termcolor import colored

class LoggerUtility:
    
    def print_debug(string):
        level = logging.DEBUG
        fmt = '[%(levelname)s] %(asctime)s - %(message)s'
        datefmt='%Y-%m-%d %H:%M:%S'
        
        logging.basicConfig(level=level, format=fmt, datefmt=datefmt)
        if "https://" in string:
            return logging.debug(colored(string, "cyan"))
        else:
            return logging.debug(colored(string, "green"))
        
        
    def print_error(string):
        level = logging.ERROR
        fmt = '[%(levelname)s] %(asctime)s - %(message)s'
        datefmt='%Y-%m-%d %H:%M:%S'
        
        logging.basicConfig(level=level, format=fmt, datefmt=datefmt)
        if level == 40:
            return logging.error(colored(string, "red"))
        else:
            return logging.exception(colored(string, "red"))