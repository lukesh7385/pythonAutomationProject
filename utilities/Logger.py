import inspect
import logging


class LogGen:
    @staticmethod
    def loggen():
        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        # create console handler or file handler and set the log level
        fh = logging.FileHandler(filename='.\\Logs\\automation_cart.log')
        # create formatter - how you want our logs to be formatted
        formatter = logging.Formatter('%(asctime)s | %(levelname)9s | %(filename)s:%(lineno)d | %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)
        return logger
