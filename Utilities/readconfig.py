

import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")




class ReadConfig:
    @staticmethod
    def get_username():
        return config.get("login","username")

    @staticmethod
    def get_password():
        return config.get("login","password")

    @staticmethod
    def get_login_url():
        return config.get("urls","login_url")