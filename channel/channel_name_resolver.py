#!/usr/bin/env python

import logging

from telegram import Bot

logger = logging.getLogger("c_n_r")


class ChannelNameResolver(object):
    def __init__(self, config):
        self.config = config
        self.bots = []


    def initialize(self):
        resolver_bot_tokens = self.config.get("name_resolver").get("bot_tokens")
        for token in resolver_bot_tokens:
            bot = Bot(token)
            logger.info(bot.get_me())
            self.bots.append(bot)


    def resolve(self, channel_name, force = False):
        return self.get_channel_details(channel_name)


    def get_channel_details(self, channel_name):
        bot = self.get_random_bot()
        try:
            chat = bot.get_chat(channel_name)
            return chat.to_json()
        except Exception as e:
            return str(e)


    def get_random_bot(self):
        return self.bots[0]
