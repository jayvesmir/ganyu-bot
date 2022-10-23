import logging
logger = logging.getLogger('discord')

class log:
    
    def info(msg: str):
        logger.getChild('Ganyu').info(msg)
        
    def warning(msg: str):
        logger.getChild('Ganyu').warning(msg)
        
    def warn(msg: str):
        logger.getChild('Ganyu').warn(msg)
        
    def error(msg: str):
        logger.getChild('Ganyu').error(msg)