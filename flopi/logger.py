import logging as _logging

# Logging levels
NOTSET    = 0  # Python
TRACE     = 5  # custom           Verbose debugging messages
DEBUG     = 10 # syslog / Python  Debug-level messages
VERBOSE   = 15 # custom
INFO      = 20 # syslog / Python
NOTICE    = 25 # syslog           Normal but significant
WARNING   = 30 # syslog / Python
ERROR     = 40 # syslog / Python
CRITICAL  = 50 # syslog / Python
ALERT     = 60 # syslog           Action must be taken immediately
EMERGENCY = 70 # syslog           System is unusable

# Register customized logging levels
_logging.addLevelName(TRACE, "TRACE")
_logging.addLevelName(VERBOSE, "VERBOSE")
_logging.addLevelName(NOTICE, "NOTICE")
_logging.addLevelName(ALERT, "ALERT")
_logging.addLevelName(EMERGENCY, "EMERGENCY")

_loggers = {}

class Python_Logger:
    """
    Python logger class.
    """
    def __init__(self, name):
        self._logger = _logging.getLogger(name)

    def set_level(self, level: int):
        """
        Set the logging level.

        Args:
          level: New logging level
        """
        return self._logger.setLevel(level)
    setLevel = set_level
    
    def is_enabled_for(self, level: int) -> bool:
        """
        Determine if the logger is enabled for the specified level.

        Args:
          level: Logging level to query

        Returns:
          Whether the logger is enabled for the level or not
        """
        return self._logger.isEnabledFor(level)
    isEnabledFor = is_enabled_for
    
    def get_effective_level(self):
        return self._logger.getEffectiveLevel()
    getEffectiveLevel = get_effective_level
    
    def trace(self, msg, *args, **kwargs):
        return self.log(TRACE, msg, *args, **kwargs)
    
    def debug(self, msg, *args, **kwargs):
        return self.log(DEBUG, msg, *args, **kwargs)
    
    def verbose(self, msg, *args, **kwargs):
        return self.log(VERBOSE, msg, *args, **kwargs)
    
    def info(self, msg, *args, **kwargs):
        return self.log(INFO, msg, *args, **kwargs)
    
    def notice(self, msg, *args, **kwargs):
        return self.log(NOTICE, msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        return self.log(WARNING, msg, *args, **kwargs)
    
    def error(self, msg, *args, **kwargs):
        return self.log(ERROR, msg, *args, **kwargs)
    
    def critical(self, msg, *args, **kwargs):
        return self.log(CRITICAL, msg, *args, **kwargs)
    
    def alert(self, msg, *args, **kwargs):
        return self.log(ALERT, msg, *args, **kwargs)
    
    def emergency(self, msg, *args, **kwargs):
        return self.log(EMERGENCY, msg, *args, **kwargs)
    
    def log(self, level, msg, *args, end="\n", **kwargs):
        msg = msg + end
        return self._logger.log(level, msg, *args, **kwargs)
    
def get_logger(name=None):
    logger = _loggers.get(name)
    if logger is None:
        logger = Python_Logger(name)
        _loggers[name] = logger
    return logger
getLogger = get_logger

def get_level_name(level):
    return _logging.getLevelName(name)
getLevelName = get_level_name

# Not in standard logging module
def set_logging_level_for(name, level):
    logger = get_logger(name)
    logger.set_level(level)
setLoggingLevelFor = set_logging_level_for

# Not in standard logging module
def set_logging_level(level):
    set_logging_level_for(None, level)
setLoggingLevel = set_logging_level

# Disable automatic newline to make logging work like print()
# Note that this affects any standard Python loggers as well, so this
# should probably be implemented in another way in the future.
_logging.StreamHandler.terminator = ""

# Set up the default logging behavior
_logging.basicConfig(style="{", level=INFO, format="")
