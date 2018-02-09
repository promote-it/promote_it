#!/usr/bin/env python
# encoding: utf-8

import json
import logging
import requests

from bot_framework.botaction import *
from bot_framework.botrequest import *
from bot_framework.node import Node
from bot_framework.util import smartkeyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Chat


class ChannelDescRequestNode(Node):
    def __init__(self):
        self.logger = logging.getLogger("cdn")
        pass


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):
        return (BotRequest(text="Now send description of %s channel" % (cwf.conversation.data.name),
                           options=self.getMarkup(),
                           cid=cwf.conversation.chatid),
                BotAction())


    def handleUserResponse(self, newResponse, cwf):
        channel_description = newResponse.update.message.text
        self.logger.info(channel_description)
        validated = self.validate_description(channel_description)
        if not validated:
            return "InvalidChannelDescNode"
        else:
            return "ChannelAdminRequestNode"


    def validate_description(self, channel_description):
        return True
