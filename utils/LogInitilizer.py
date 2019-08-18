from loguru import logger
import sys

class LogInitilizer:

    __instance = False

    @staticmethod
    def getLogger():
        isLogInitialized=False
        if not LogInitilizer.__instance:
            LogInitilizer.__instance=True
            file_name = './info.log'
            format = "\n{level} | {time:YYYY-MM-DD at HH:mm:ss} | {name} | {function} | {line} | {message}"

            logger.add(sink=file_name, format=format, rotation="30 days", filter=None,
                          colorize=None, serialize=False, backtrace=True, enqueue=True, catch=False,level='INFO')

            logger.add(sink=sys.stdout, format=format, filter=None,
                          colorize=None, serialize=False, backtrace=True, enqueue=True, catch=False,level='INFO')

            logger.add(sink=sys.stderr, format=format, filter=None,
                          colorize=None, serialize=False, backtrace=True, enqueue=True, catch=False,level='INFO')
        return logger

