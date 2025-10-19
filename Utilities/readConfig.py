from configparser import ConfigParser
def read_config(section,value):
    config=ConfigParser()
    config.read(r'C:\Users\tilak\PycharmProjects\CarWalePOM\ConfigurationData\config.ini')
    return config.get(section,value)