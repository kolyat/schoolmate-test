import logging.config

from utils import service


#
# Defaults
#

DEFAULT_TARGET_CONFIG = {
    'default': {
        'protocol': 'http',
        'server': 'localhost:8000',
        'users': {
            'default': {
                'username': 'admin',
                'password': 'nimda',
                'mail_server': 'pop.gmail.com'
            }
        }
    }
}

DEFAULT_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s | [%(levelname)8s] | '
                      '%(module)s.%(funcName)s(%(lineno)d) - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        },
        'http_file': {
            'class': 'logging.FileHandler',
            'filename': './logs/http.log',
            'formatter': 'standard',
            'level': 'DEBUG',
            'mode': 'a'
        }
    },
    'loggers': {
        'urllib3': {
            'handlers': ['http_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'http.client': {
            'handlers': ['http_file'],
            'level': 'DEBUG',
            'propagate': False
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}


#
# Init
#

current_config = service.Config()
current_config.update_config('config.json')

logging.config.dictConfig(current_config.logging)
service.httpclient_logging_patch()
