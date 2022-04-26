import os
import sys
import time
import inspect
from loguru import logger
from seldom.running.config import BrowserConfig
from seldom.running.config import Seldom

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
exec_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(exec_dir, "reports")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
if BrowserConfig.LOG_PATH is None:
    BrowserConfig.LOG_PATH = os.path.join(report_dir, "seldom_log.log")
if BrowserConfig.REPORT_PATH is None:
    BrowserConfig.REPORT_PATH = os.path.join(report_dir, now_time + "_result.html")


class Logger:
    def __init__(self, level: str = "DEBUG", colorlog: bool = True):
        self.logger = logger
        self._colorlog = colorlog
        self._console_format = "[<fg #FA8072>{level}</> <green>{time:YYMMDD HH:mm:ss}</green>] <level>{message}</level>"
        self._log_format = "[{level} {time: YYMMDD HH:mm:ss}] {message}"
        self._level = level
        self.logfile = BrowserConfig.LOG_PATH
        self.set_level(self._colorlog, self._console_format, self._level)

    def set_level(self, colorlog: bool = True, format: str = None, level: str = "DEBUG"):
        if format is None:
            format = self._console_format
        logger.remove()
        logger.add(sys.stderr, level=level, colorize=colorlog, format=format)
        logger.add(self.logfile, level=level, colorize=colorlog, format=self._log_format, encoding="utf-8")

    def trace(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [TRACE] " + str(msg))
        return self.logger.trace(msg)

    def debug(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [DEBUG] " + str(msg))
        return self.logger.debug(msg)

    def info(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [INFO] " + str(msg))
        return self.logger.info(msg)

    def success(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [SUCCESS] " + str(msg))
        return self.logger.success(msg)

    def warn(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [WARNING] " + str(msg))
        return self.logger.warning(msg)

    def error(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [ERROR] " + str(msg))
        return self.logger.error(msg)

    def critical(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [CRITICAL] " + str(msg))
        return self.logger.critical(msg)

    def printf(self, msg: str):
        return self.logger.success(msg)


log = Logger(level="DEBUG")
