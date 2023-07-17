import socket
import logging

from version import __version__
from src.configs.configs import configs

__hostname__ = socket.gethostname()


class RunInfoFormatter(logging.Formatter):

  def format(self, record):
    if not record.__dict__.get('run_info'):
      run_info = {}
      run_info['version'] = __version__
      run_info['hostname'] = __hostname__
      run_info['instance'] = configs['instance']
      run_info['app_name'] = configs['app_name']
      record.__dict__['run_info'] = run_info

    return logging.Formatter.format(self, record)
