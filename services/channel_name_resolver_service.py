#!/usr/bin/env python

import json
import logging


import sys
from klein import Klein

from channel.channel_name_resolver import ChannelNameResolver
from config.promote_it_config import PromoteItConfig

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger("name_resolver")

config = PromoteItConfig()
app = Klein()
resolver = ChannelNameResolver(config)


@app.route('/resolve/<channel_name>', methods=['GET'])
def resolve(request, channel_name):
    return resolver.resolve(channel_name)


@app.route('/force_resolve/<channel_name>', methods=['GET'])
def force_resolve(request, channel_name):
    return resolver.resolve(channel_name, force=True)


@app.route('/update/<channel_name>', methods=['POST'])
def update(request, channel_name):
    return channel_name


def usage():
    print("./script env")
    sys.exit(-1)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        usage()

    env = sys.argv[1]
    config.initialize("config/promote_it.yml", "config/" + env + "_promote_it.yml")

    resolver.initialize()

    host = config.get("name_resolver").get("host")
    port = int(config.get("name_resolver").get("port"))

    app.run(host, port)
