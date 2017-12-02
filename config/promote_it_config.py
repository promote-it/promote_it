#!/usr/bin/env python

import yaml


class PromoteItConfig(object):

    def __init__(self):
        self.config_file = None
        self.config = {}


    def initialize(self, config_file):
        self.config_file = config_file
        self.load_config_file()


    def load_config_file(self):
        print("Loading config file %s" % self.config_file)
        self.config = yaml.load(open(self.config_file, 'r'))


    def get(self, source):
        source_config = self.config.get(source)
        return source_config


    def print(self):
        print(self.config)


    def print_sections(self):
        for section in self.config:
            print(section)

config = PromoteItConfig()

if __name__ == "__main__":
    config = PromoteItConfig()
    config.initialize("../services/dev.yml")
    config.print()
    config.print_sections()


#        #    def __init__(self):
#        self.promote_it_share_bot_token = "326265151:AAH3iQP6__6FhDFx1KMVMMXQGz2hXP55I4c"
#        self.channel_resolver_bot_tokens = [
#            "122065802:AAE9psorrr79jTynQwFuOMbocNETs2m-MM8",
#            "105656295:AAG9rg-XtG68Ath5x1034IhSesNgDQKpMyc",
#        ]
#        self.promote_it_bot_token = ""
#        self.resolve_age = 10

#config = PromoteItConfig()