import logging

class Logger_Class:

   @staticmethod
   def get_loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(funcName)s : %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('.\\Logs\\OrangeHRM.log')
        handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(file_handler)
        return logger

