#!/usr/bin/env python

import logging

from telegram import Bot

logger = logging.getLogger("c_a_r")


class ChannelAdminResolver(object):
    def __init__(self, config):
        self.bot = None
        self.config = config


    def initialize(self):
        self.bot = Bot(self.config.get("admin_resolver").get("bot_token"))
        logger.info(self.bot.get_me())


    def resolve(self, channel_name, force = False):
        admins = self.get_chat_administrators(channel_name)
        return self.channel_has_admin_previlages(channel_name, admins)


    def get_chat_administrators(self, channel_name):
        try:
            return self.bot.get_chat_administrators(channel_name)
        except Exception as e:
            return []


    def channel_has_admin_previlages(self, channel_name, chats):
        if (chats == None):
            return False

        if (len(chats) < 1):
            return False

        for chat in chats:
            if (chat.user.username == self.bot.username):
                if (chat.status == chat.ADMINISTRATOR):
                    if (chat.can_edit_messages and chat.can_post_messages):
                        return True

        return False
