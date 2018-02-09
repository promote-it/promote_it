#!/usr/bin/env python
# encoding: utf-8

from bot_framework.botaction import *
from bot_framework.node import Node
from telegram import ParseMode


class ChannelConfirmNode(Node):
    def __init__(self):
        pass


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):
        query = userresponse.update.callback_query
        text = "Confirmed"
        cwf.bot.edit_message_text(
            text=text,
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            parse_mode = ParseMode.HTML
        )
        return (None, BotAction())


    def handleUserResponse(self, newResponse, cwf):
        return "StartNode"


    def handleTimerResponse(self, timerresponse, cwf):
        pass