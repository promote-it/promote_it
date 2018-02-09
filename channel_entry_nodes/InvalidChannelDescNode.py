#!/usr/bin/env python
# encoding: utf-8

from bot_framework.botaction import *
from bot_framework.botrequest import *
from bot_framework.node import Node
from bot_framework.util import smartkeyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class InvalidChannelDescNode(Node):
    def __init__(self):
        pass


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):
        return (BotRequest(text="channel desc is invalid. please /start to resubmit",
                           options=self.getMarkup(),
                           cid=cwf.conversation.chatid),
                BotAction())


    def handleUserResponse(self, newResponse, cwf):
        return "StartNode"


    def resolve_channel_name(self):
        return True