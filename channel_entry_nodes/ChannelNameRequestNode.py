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


class ChannelNameRequestNode(Node):
    def __init__(self):
        self.logger = logging.getLogger("cdn")
        pass


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):
        return (BotRequest(text="%s,\n\nPlease send me your channel name (with @)" % (cwf.conversation.username),
                           options=self.getMarkup(),
                           cid=cwf.conversation.chatid),
                BotAction())


    def handleUserResponse(self, newResponse, cwf):
        channel_name = newResponse.update.message.text
        self.logger.info(channel_name)
        resolved = self.resolve_channel_name(channel_name, cwf)
        if not resolved:
            return "ChannelNameRequestNode"
        else:
            return "ChannelDescRequestNode"


    def resolve_channel_name(self, channel_name, cwf):
        channel_resolver_host = cwf.config.get("name_resolver").get("host")
        channel_resolver_port = cwf.config.get("name_resolver").get("port")
        url = "http://%s:%s/resolve/%s" % (channel_resolver_host, channel_resolver_port, channel_name)
        result = requests.get(url).text
        channel = Chat.de_json(json.loads(result), None)
        self.logger.info(channel)
        cwf.conversation.data.name = "@" + channel.username
        if channel.type == "channel":
            return True
        else:
            return False
