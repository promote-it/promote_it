#!/usr/bin/env python

import logging
import sys

from config.promote_it_config import PromoteItConfig
from bot_framework import TwistedUpdater
from bot_framework import WorkflowManager, UserResponse
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from twisted.internet import reactor
from object_types.channel import Channel

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger("channel_entry_bot")

config = PromoteItConfig()
wfmgr = WorkflowManager(None)


def get_chat_id_username(update):
    chatid = None
    username = None

    if update.message is not None:
        chatid = update.message.chat_id
        username = update.message.from_user.username
    elif update.callback_query is not None:
        chatid = update.callback_query.message.chat_id
        username = update.callback_query.from_user.username

    return chatid, username


def get_from_user_id(update):
    if update.message is not None:
        return update.message.from_user.id
    elif update.callback_query is not None:
        return update.callback_query.from_user.id

    return None


def everything(bot, update):
    logger.info(update)

    chatid, username = get_chat_id_username(update)

    wf = wfmgr.getWorkflow("channel_entry_", chatid, username, None)
    wf.handleUserResponse(UserResponse(update))


def start(bot, update):
    logger.info(update)

    chatid, username = get_chat_id_username(update)
    wf = wfmgr.getWorkflow("channel_entry_", chatid, username, None)

    wf.config = config
    wf.reset()
    wf.conversation.data = Channel()

    wf.handleUserResponse(UserResponse(update))


def error_function(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
    logger.error(error)



def usage():
    print("./script env")
    sys.exit(-1)


def main():
    if (len(sys.argv) < 2):
        print("./script env")
        sys.exit(-1)
        usage()

    env = sys.argv[1]

    config.initialize("config/promote_it.yml", "config/" + env + "_promote_it.yml")

    token = config.get("channel_entry_bot").get("token")
    updater = TwistedUpdater(token)
    logger.info(updater.bot.get_me())
    wfmgr.bot = updater.bot

    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.dispatcher.add_handler(MessageHandler(Filters.all, everything))
    updater.dispatcher.add_handler(CallbackQueryHandler(everything))
    updater.dispatcher.add_error_handler(error_function)
    updater.start_polling(poll_interval=1.0, clean=True)

    reactor.run()


if __name__ == "__main__":
    main()