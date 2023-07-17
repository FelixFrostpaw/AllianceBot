import logging
import src.configs.secrets as secrets
from logtail import LogtailHandler
from src.logging.run_info_formatter import RunInfoFormatter


def create_betterstack_handler():
  betterstack_token = secrets.betterstack_token
  handler = LogtailHandler(source_token=betterstack_token)
  return handler


def create_logger(name, handler, formatter):
  handler.setFormatter(formatter)
  logger = logging.getLogger(name)
  logger.handlers = []
  logger.addHandler(handler)
  return logger


def create_bot_logger(name, level=None):
  handler = create_betterstack_handler()
  formatter = RunInfoFormatter()
  logger = create_logger(name, handler, formatter)

  if level:
    logger.setLevel(level)

  return logger
