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


class ChannelAdminRequestNode(Node):
    def __init__(self):
        self.logger = logging.getLogger("cdn")
        pass


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):
        resolved = self.resolve_channel_admin(cwf)
        if not resolved:
            return (BotRequest(text="%s,\n\nPlease send me your channel name (with @)" % (cwf.conversation.username),
                               options=self.getMarkup(),
                               cid=cwf.conversation.chatid),
                    BotAction())
        else:
            return (None, BotAction(cflow=True))


    def handleUserResponse(self, newResponse, cwf):
        return "ChannelConfirmRequestNode"


    def resolve_channel_admin(self, cwf):
        channel_name = cwf.conversation.data.name
        channel_resolver_host = cwf.config.get("admin_resolver").get("host")
        channel_resolver_port = cwf.config.get("admin_resolver").get("port")
        url = "http://%s:%s/resolve/%s" % (channel_resolver_host, channel_resolver_port, channel_name)
        result = requests.get(url).text

        if bool(result) == True:
            return True
        else:
            return False
