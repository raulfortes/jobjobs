import ConfigParser
from logging.config import fileConfig as log_config_read

base_path = '.'
config_file = 'system.conf'
parameters = ConfigParser.RawConfigParser()


def load(filename=None):
    if filename != None:
        config_file = filename

    #Load or reload config
    parameters.read(config_file)
    log_config_read(config_file)
