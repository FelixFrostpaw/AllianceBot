from secrets import discord_bot_token

from alliance_bot import bot

import logging
from run_info_formatter import RunInfoFormatter
import logger_factory

bot.run(token=discord_bot_token,
        log_handler=logger_factory.create_betterstack_handler(),
        log_formatter=RunInfoFormatter(),
        log_level=logging.DEBUG,
        root_logger=False)
