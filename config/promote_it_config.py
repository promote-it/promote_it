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