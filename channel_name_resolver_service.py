#!/usr/bin/env python

import json
from klein import Klein
from channel_name_resolver import ChannelNameResolver


app = Klein()
resolver = ChannelNameResolver()


@app.route('/resolve/<channel_name>', methods=['GET'])
def resolve(request, channel_name):
    return json.dumps(resolver.resolve(channel_name))


@app.route('/force_resolve/<channel_name>', methods=['GET'])
def force_resolve(request, channel_name):
    return json.dumps(resolver.resolve(channel_name, force=True))


@app.route('/update/<channel_name>', methods=['POST'])
def update(request, channel_name):
    return channel_name


if __name__ == "__main__":
    resolver.initialize()
    app.run('localhost', 9000)
