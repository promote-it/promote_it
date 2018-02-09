#!/usr/bin/env python
# encoding: utf-8

from bot_framework.botaction import *
from bot_framework.node import Node

class StartNode(Node):
    def __init__(self):
        self.acceptedCommands = ["/start"]


    def canHandle(self, userresponse):
        return True


    def buildBotRequest(self, userresponse, cwf):
        return (None, BotAction(cflow=True))


    def handleUserResponse(self, newResponse, cwf):
        return "ChannelNameRequestNode"