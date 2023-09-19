#!/usr/bin/env python3
# @author      Markus Kösters

import logging

from Logging.LoggingInterface import LoggingInterface


class Logger(LoggingInterface):
    logging.basicConfig(level=logging.INFO, filename='Logging.log', filemode='w', format='%(asctime)s | [%(levelname)s] %(message)s')

    def __logFormatter(self, fileHandler: logging.FileHandler) -> None:
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
        fileHandler = logging.FileHandler(f'{moduleName}.log')
        self.__logFormatter(fileHandler)
        return fileHandler

    def createLogEntry(self, logLevel: str, moduleName: __name__, message: str):
        """
        Creating a log-entry using the Logging-module
        :return:
        """
        logger = logging.getLogger(moduleName)
        if not logger.hasHandlers():
            fileHandler = self.__fileHandler(moduleName)
            logger.addHandler(fileHandler)
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
