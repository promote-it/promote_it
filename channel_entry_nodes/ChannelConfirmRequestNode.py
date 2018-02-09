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


class ChannelConfirmRequestNode(Node):
    def __init__(self):
        self.logger = logging.getLogger("cdn")
        pass


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):

        return (BotRequest(text="Confirm?",
                           options=self.getMarkup(),
                           cid=cwf.conversation.chatid),
                BotAction())


    def handleUserResponse(self, newResponse, cwf):
        query = newResponse.update.callback_query
        if query.data == "CANCEL":
            return "ChannelCancelNode"
        if query.data == "CONFIRM":
            return "ChannelConfirmNode"


    def getMarkup(self):
        options = ["CONFIRM", "CANCEL"]

        inline_keyboard = []
        for option in options:
            inline_keyboard.append(InlineKeyboardButton(option, callback_data=option))

        keyboard = smartkeyboard(inline_keyboard)
        reply_markup = InlineKeyboardMarkup(keyboard)

        return reply_markup
