#!/usr/bin/env python

import json

import sys
from klein import Klein

from admin.channel_admin_resolver import ChannelAdminResolver
from config.promote_it_config import  config

app = Klein()
resolver = ChannelAdminResolver()


@app.route('/resolve/<channel_name>', methods=['GET'])
def resolve(request, channel_name):
    return json.dumps(resolver.resolve(channel_name))


@app.route('/force_resolve/<channel_name>', methods=['GET'])
def force_resolve(request, channel_name):
    return json.dumps(resolver.resolve(channel_name, force=True))


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
    config.initialize("config/" + env + ".yml")

    resolver.initialize()

    host = config.get("admin_resolver").get("host")
    port = int(config.get("admin_resolver").get("port"))

    app.run(host, port)
