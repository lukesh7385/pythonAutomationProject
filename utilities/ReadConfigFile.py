import configparser

config = configparser.RawConfigParser()

config.read(".\\Configuration\\Config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password
