#!/usr/bin/env python3
# @author      Markus Kösters

import logging

from Logging.LoggingInterface import LoggingInterface


class Logger(LoggingInterface):
    """
    Class for making easy access to logging from any module.
    """
    loggers: list = []
    logLevel = logging.INFO

    @staticmethod
    def __logFormatter(fileHandler: logging.FileHandler) -> None:
        """
        Method for applying the correct logging-format before writing the message into a file.
        :return: Formatter caring for the correct format of the logs.
        """
        formatter_ = logging.Formatter('%(asctime)s | [%(levelname)s] %(message)s')
        fileHandler.setFormatter(formatter_)

    def __fileHandler(self, moduleName: str) -> logging.FileHandler:
        """
        TODO: format the name!!!!
        Method for creating a File-Handler for the logged module.
        :param moduleName: Name of the module that is getting logged. Used for creating a filename.
        :return: File-Handler that is being used to store the log-messages into.
        """
        print(moduleName)
        fileHandler = logging.FileHandler(f'{moduleName}.log', mode='w')
        self.__logFormatter(fileHandler)
        return fileHandler

    def __setupLogger(self, logger: logging.getLogger, moduleName: __name__) -> None:
        """
        Method used for configuring logger-settings.
        :param logger: Logger that shall be configured.
        :param moduleName: Name of the module that is getting logged. Used for creating a filename.
        """
        fileHandler = self.__fileHandler(moduleName)
        logger.addHandler(fileHandler)
        logger.setLevel(self.logLevel)
        self.loggers.append(logger)

    def createLogEntry(self, logLevel: str, moduleName: __name__, message: str) -> None:
        """
        Creating a log-entry into a dedicated file, using the Logging-module.
        :param logLevel:    String representing the Log-Level.
                            available: 'debug', 'info', 'warning', 'error', 'critical', 'exception'
        :param moduleName:  Name of the module that is being logged.
        :param message:     Log-Message that shall be stored.
        """
        logger = logging.getLogger(moduleName)
        if logger not in self.loggers:
            self.__setupLogger(logger, moduleName)
        match logLevel:
            case 'debug':
                logger.debug(message)
            case 'info':
                logger.info(message)
            case 'warning':
                logger.warning(message)
            case 'error':
                logger.error(message)
            case 'critical':
                logger.critical(message)
            case 'exception':
                logger.exception(message)
            # if log-level does not match any case, it is going to be written as info-level
            case _:
                logger.info(message)
