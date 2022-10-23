import logging
from logging import Logger
logger = logging.getLogger('discord').getChild('Ganyu')

class log():
    
    def __init__(self, _child: str = None):
        self._child = _child
    
    def info(self, msg: str):
        if not self._child:
            logger.info(msg)
            return
        logger.getChild(self._child).info(msg)
        
    def warning(self, msg: str):
        if not self._child:
            logger.info(msg)
            return
        logger.getChild(self._child).warning(msg)
        
    def warn(self, msg: str):
        if not self._child:
            logger.info(msg)
            return
        logger.getChild(self._child).warn(msg)
        
    def error(self, msg: str):
        if not self._child:
            logger.info(msg)
            return
        logger.getChild(self._child).error(msg)