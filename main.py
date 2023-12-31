import logging

from src.configs.configs import configs
from src.alliance_bot.alliance_bot import bot
from src.logging.run_info_formatter import RunInfoFormatter
from src.logging.logger_factory import create_betterstack_handler

bot.run(token=configs['discord_bot_token'],
        log_handler=create_betterstack_handler(),
        log_formatter=RunInfoFormatter(),
        log_level=logging.DEBUG,
        root_logger=False)
